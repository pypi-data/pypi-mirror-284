import os

def get_env_bool(key: str) -> bool:
    """ Handles the boolean environment variable assignment """
    if not key in os.environ:
        raise KeyError("No environment variable %s", key)
    
    if not os.environ[key] in ("True", "False"):
        raise AssertionError("Key %s is not proper boolean: %s", key, os.environ[key])
    
    return os.environ[key] == "True"