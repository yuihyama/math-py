#!/usr/bin/env python3


"""my sum1
"""


def my_sum1(n):
    """

    >>> my_sum1(10)
    55.0
    """
    return (1/2)*n*(n + 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
