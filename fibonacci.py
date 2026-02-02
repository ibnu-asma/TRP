"""Simple Fibonacci utility.

Provides a safe, efficient `fibonacci(n)` function returning the n-th Fibonacci
number (0-indexed: fib(0)=0, fib(1)=1).
"""
from functools import lru_cache


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed).

    Args:
        n: Non-negative integer index.

    Returns:
        int: Fibonacci number at index `n`.

    Raises:
        ValueError: If `n` is negative or not an integer.
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    # Iterative approach — O(n) time, O(1) memory
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@lru_cache(maxsize=None)
def fibonacci_recursive(n: int) -> int:
    """Recursive memoized version (for demonstration).

    Note: iterative `fibonacci` is preferred for speed and memory.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compute Fibonacci numbers")
    parser.add_argument("n", type=int, help="index (non-negative integer)")
    parser.add_argument("--recursive", action="store_true", help="use recursive memoized version")
    args = parser.parse_args()

    fn = fibonacci_recursive if args.recursive else fibonacci
    print(fn(args.n))
