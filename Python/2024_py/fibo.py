# fibo.py
def fibonacci_recursive(n):
    """Return the n-th Fibonacci number using recursion."""
    if n <= 0:
        raise ValueError("Input should be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)