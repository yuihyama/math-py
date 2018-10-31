#!/usr/bin/env python3


"""my product1
"""


def my_product1(n):
    """

    >>> my_product1(3)
    6
    >>> my_product1(10)
    3628800
    """
    res = 1
    for i in range(n):
        res *= i+1

    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
