from threading import Lock
from typing import Any


class SingletonMeta(type):

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        with cls._lock:
            if cls not in cls._instances:
                instances = super().__call__(*args, **kwds)
                cls._instances[cls] = instances
        return cls._instances[cls]
