# Fibonacci utility

This small module provides a simple, safe Fibonacci function.

Usage:

Run from Python:

```bash
python fibonacci.py 10
python fibonacci.py 10 --recursive
```

Run tests:

```bash
python test_fibonacci.py
```

Function:

- `fibonacci(n: int) -> int`: iterative, O(n) time, O(1) memory.
- `fibonacci_recursive(n: int) -> int`: recursive memoized (demo).
