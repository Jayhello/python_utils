# _*_ coding:utf-8 _*_

"""
This file is about ways to get nth column from array
"""
import numpy as np


def get_nth_column():
    """
    this is about how to get nth column from array
    :return:none
    """
    arr = np.arange(9).reshape((3, 3))
    print arr
    # [[0 1 2]
    #  [3 4 5]
    #  [6 7 8]]
    arr_c2 = arr[:, [0, 2]]  # arr_c2 deep copy from arr
    print arr_c2
    # [[0 2]
    #  [3 5]
    #  [6 8]]
    arr_c2[:, [0]] = 9
    print arr  # no change, as we see this is deep copy
    print arr_c2
    # [[9 2]
    #  [9 5]
    #  [9 8]]
    arr_c1 = arr[:, 0]
    print arr_c1

if __name__ == '__main__':
    get_nth_column()
