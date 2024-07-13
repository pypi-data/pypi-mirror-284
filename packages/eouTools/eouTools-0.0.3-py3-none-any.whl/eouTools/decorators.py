from typing import Callable, Any
from functools import wraps

def rename_on_init(name: str) -> Callable:
    """
    Rename a function when it is initialized. This may raise unexpected behavior, however
    :param name: str
    :return:
    """
    def decorator(func: Callable) -> Callable:
        func.__name__ = name

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return decorator