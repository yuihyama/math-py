#!/usr/bin/env python3


"""my sum squares2
"""


def my_sum_squares2(n):
    """

    >>> my_sum_squares2(3)
    14
    """
    return sum([i*i for i in range(n+1)])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
