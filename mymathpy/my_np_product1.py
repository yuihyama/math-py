#!/usr/bin/env python3


"""my numpy product1
"""


from numpy import prod


def my_np_product1(n):
    """

    >>> my_np_product1(3)
    6
    >>> my_np_product1(10)
    3628800
    """
    n_list = list(range(n+1))

    if 0 in n_list:
        n_list.remove(0)

    return prod(n_list)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
