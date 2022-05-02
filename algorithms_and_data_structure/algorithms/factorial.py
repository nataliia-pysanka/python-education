"""
Recursive factorial implementation
"""


def factorial(n):
    if n < 0:
        raise ValueError('The number entered must be positive!')
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)
