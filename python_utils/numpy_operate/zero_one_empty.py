# coding:utf-8

import numpy as np


def empty_test():
    arr = np.array([[2.5, 3, 1], [1.1, -2, 3]])
    print arr

    print np.empty_like(arr)

    print np.empty([2, 2])
    # [[2.02554939e-316   2.50034710e-315]
    #  [1.97872580e-316   2.00283462e-316]]

    print np.empty([2, 2], dtype=int)
    # [[58157000   0]
    #  [58157064  0]]


def zero_test():
    print np.zeros(5)
    # [ 0.  0.  0.  0.  0.]
    print np.zeros((5,), dtype=np.int)
    # [0 0 0 0 0]
    print np.zeros((2, 1))
    # [[ 0.]
    #  [ 0.]]
    x = np.arange(6).reshape((2, 3))
    print np.zeros_like(x)
    # [[0 0 0]
    #  [0 0 0]]

if __name__ == '__main__':
    # empty_test()
    zero_test()
    pass
