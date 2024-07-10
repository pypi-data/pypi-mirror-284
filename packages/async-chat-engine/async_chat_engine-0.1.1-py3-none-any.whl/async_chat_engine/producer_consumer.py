import asyncio
import logging
import uuid
import json

from .chat_engine import ChatEngine


class ProducerConsumer:
    logger = logging.getLogger("main")

    def __init__(self, num_consumers: int, engine: ChatEngine) -> None:
        self.logger.info("Creating ProducerConsumer object")
        self.queue = asyncio.Queue()
        self.num_consumers = num_consumers
        self.chat_engine = engine
        self.initialised = False

    async def init_consumers(self):
        if not self.initialised:
            self.logger.info("Initialising consumers")
            self.consumers = [
                asyncio.create_task(self.consume()) for _ in range(self.num_consumers)
            ]
            self.initialised = True

    async def close_consumers(self):
        for consumer in self.consumers:
            consumer.cancel()
        await asyncio.gather(*self.consumers, return_exceptions=True)
        self.logger.info("Consumers closed")
        self.initialised = False

    async def produce(self, message):
        self.logger.info("Producing message: %s", message)
        await self.queue.put(message)

    async def consume(self):
        self.logger.info("Consuming messages")
        sampling_params = self.chat_engine.create_sampling_params()
        while True:
            # Get message from queue
            message = await self.queue.get()
            self.logger.info("Got message from queue: %s", message)
            try:
                # Unpack message
                query, user_id, websocket = message

                # Create prompt for engine
                self.chat_engine.update_chat_history(user_id, "user", query)
                prompt = self.chat_engine.create_prompt(user_id)

                # Process message
                stream = await self.chat_engine.engine.add_request(
                    uuid.uuid4().hex, prompt, sampling_params
                )

                self.logger.info("Stream created for User: %s %s", user_id, stream)

                # Process output
                cursor = 0
                output = ""
                async for request_output in stream:
                    output += request_output.outputs[0].text[cursor:]

                    await websocket.send(json.dumps({"message": output, "status": "generating"}))

                    cursor = len(request_output.outputs[0].text)

                await websocket.send(json.dumps({"message": output, "status": "complete"}))
                self.chat_engine.update_chat_history(user_id, "assistant", output)
                self.logger.info(
                    "Completed request for User: %s, %s",
                    user_id,
                    output,
                )
            except Exception as e:
                self.logger.error("Error processing message: %s", e)
            finally:
                # Mark task as done
                self.queue.task_done()
