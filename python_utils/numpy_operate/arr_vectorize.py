# coding:utf-8

import numpy as np


def my_fun(a, b):
    if a >= b:
        return a - b
    else:
        return a + b


def test_vectorize():
    v_fun = np.vectorize(my_fun)
    arr = np.arange(8).reshape(2, 4)
    print arr
    # [[0 1 2 3]
    #  [4 5 6 7]]
    print v_fun(arr, 4)
    # [[4 5 6 7]
    #  [0 1 2 3]]

if __name__ == '__main__':
    test_vectorize()
    pass
