#!/usr/bin/env python3


"""my factorial
"""


def my_factorial1(n):
    """

    >>> my_factorial1(1)
    1
    >>> my_factorial1(0)
    1
    >>> my_factorial1(-1)
    1
    >>> my_factorial1(5)
    120
    """
    if n < 2:
        return 1
    else:
        return n * my_factorial1(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
