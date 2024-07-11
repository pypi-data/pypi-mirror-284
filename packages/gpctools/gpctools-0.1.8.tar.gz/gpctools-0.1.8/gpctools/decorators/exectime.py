from typing import Callable
from functools import wraps
from time import perf_counter


def exectime(func: Callable) -> Callable:
    """
    Decorator that prints the running time of a function or method
    Args: func (Callable): any function or method;
    Returns: the same func;
    Prints: Running time;
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        start_time: float = perf_counter()
        func(*args, **kwargs)
        end_time: float = perf_counter()
        print(f"exectime: {func.__name__}() took {end_time - start_time:.3f}s to run.")

    return wrapper
