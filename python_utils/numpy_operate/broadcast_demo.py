# coding:utf-8

import numpy as np


def broadcast_demo():
    arr = np.ones((3, 4))
    print arr
    print arr + 1

    b = np.broadcast(arr, 1)
    print b.shape
    # (3L, 4L)


def bc_demo_2():
    a = np.array([1.0, 2.0, 3])
    b = np.ones(3) * 2
    print b
    # [ 2.  2.  2.]
    print a * b
    # [ 2.  4.  6.]

    b = 2
    print a * b
    # [ 2.  4.  6.]

    x = np.arange(4).reshape(4, 1)
    print x
    # [[0]
    #  [1]
    #  [2]
    #  [3]]
    y = np.ones(5)
    print y
    # [ 1.  1.  1.  1.  1.]
    z = x + y
    print z
    # [[ 1.  1.  1.  1.  1.]
    #  [ 2.  2.  2.  2.  2.]
    #  [ 3.  3.  3.  3.  3.]
    #  [ 4.  4.  4.  4.  4.]]
    print z.shape
    # (4L, 5L)

if __name__ == '__main__':
    # broadcast_demo()
    bc_demo_2()
    pass
