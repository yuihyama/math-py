#!/usr/bin/env python3


"""my sum squares1
"""


def my_sum_squares1(n):
    """

    >>> my_sum_squares1(3)
    14.0
    """
    return (1/6)*n*(n + 1)*(2*n + 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
