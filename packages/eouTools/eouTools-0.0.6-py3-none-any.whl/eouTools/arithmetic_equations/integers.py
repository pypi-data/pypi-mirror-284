import numpy as np

def factorial(n: int) -> int:
    """
    Calculate the factorial of a number
    :param n: int
    :returns: int
        """
    n = np.abs(n)

    return np.prod(np.arange(1, n + 1, dtype = int))

def fib(n: int) -> int:
    """
    Calculate the fibonacci sequence for a number recursively
    :param n: int
    :returns: int
    """
    n = np.abs(n)
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
