#!/usr/bin/env python3


"""my sum2
"""


def my_sum2(n):
    """

    >>> my_sum2(10)
    55
    """
    res = 0
    for i in range(n+1):
        res += i

    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
