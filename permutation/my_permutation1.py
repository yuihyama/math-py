#!/usr/bin/env python3


"""my permutation1
"""


from my_factorial1 import my_factorial1


def my_permutation1(n, r):
    """

    >>> my_permutation1(10, 3)
    120
    """
    return my_factorial1(n) / my_factorial1(n - r)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
