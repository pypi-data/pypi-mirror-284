from typing import Callable, Any, Dict
from functools import wraps

class MemoizedFunction:
    def __init__(self, func: Callable):
        self.func = func
        self.cache: Dict[str, Any] = {}

    def delete_cache(self) -> None:
        self.cache = {}

    def __call__(self, *args, **kwargs) -> Any:
        key = str(args) + str(kwargs)
        if key not in self.cache:
            self.cache[key] = self.func(*args, **kwargs)
        return self.cache[key]

    def __getattr__(self, name: str) -> Any:
        return getattr(self.func, name)

def memoize(func: Callable) -> MemoizedFunction:
    """Create a cache of all results given by a function. run the `.delete_cache()` function to delete the cache. Can be used to speed up certain algorithms such as recursive Fibonacci sequence"""
    memoized_function = MemoizedFunction(func)
    return memoized_function

def rename_on_init(name: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        func.__name__ = name

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return decorator
