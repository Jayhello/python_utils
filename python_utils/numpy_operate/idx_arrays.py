# coding:utf-8

import numpy as np


def single_idx():
    arr = np.arange(6)
    print arr
    # [0 1 2 3 4 5]
    print arr[1], arr[-1]
    # 1 5
    arr2 = np.arange(10)
    print arr2
    # [0 1 2 3 4 5 6 7 8 9]
    print arr2[2: 5], arr2[:-7], arr2[1: 7: 2]
    # [2 3 4] [0 1 2] [1 3 5]

    b = arr2 > 7
    print b
    # [False False False False False False False False  True  True]
    print arr2[b]
    # [8 9]


def multidimen_idx():
    arr = np.arange(6)
    print arr
    # [0 1 2 3 4 5]
    arr.shape = (2, 3)
    print arr
    # [[0 1 2]
    #  [3 4 5]]

    print arr[1, 1], arr[1, -1]
    # 4 5
    print arr[1], arr[1][1]
    # [3 4 5] 4

    arr2 = np.arange(35).reshape(5, 7)
    print arr2
    # [[ 0  1  2  3  4  5  6]
    #  [ 7  8  9 10 11 12 13]
    #  [14 15 16 17 18 19 20]
    #  [21 22 23 24 25 26 27]
    #  [28 29 30 31 32 33 34]]

    print arr2[1:5:2]
    # [[ 7  8  9 10 11 12 13]
    #  [21 22 23 24 25 26 27]]

    # 1:5:2 means row 2, 4, ::3 means every 3 column
    print arr2[1:5:2, ::3]
    # [[ 7 10 13]
    #  [21 24 27]]

    print arr2[np.array([0, 2, 4]), 1:3]
    # [[ 1  2]
    #  [15 16]
    #  [29 30]]

    print arr2[np.array([0, 2, 4]), np.array([0, 1, 2])]
    # [ 0 15 30]

    print arr2[np.array([0, 2, 4]), 1]
    # [ 1 15 29]

    b = arr2 > 20
    print arr2[b]
    # [21 22 23 24 25 26 27 28 29 30 31 32 33 34]


def n_dimension_arr():
    arr = np.arange(30).reshape(2, 3, 5)
    print arr
    # [[[ 0  1  2  3  4]
    #   [ 5  6  7  8  9]
    #  [10 11 12 13 14]]
    #
    # [[15 16 17 18 19]
    #  [20 21 22 23 24]
    # [25 26 27 28 29]]]


def assign_val():
    arr = np.arange(10)
    print arr
    # [0 1 2 3 4 5 6 7 8 9]
    arr[2:7] = 1
    print arr
    # [0 1 1 1 1 1 1 7 8 9]
    arr[2:7] = range(5)
    print arr
    # [0 1 0 1 2 3 4 7 8 9]　


def np_argmax():
    arr = np.array([1, 5, 3])
    print np.argmax(arr)


if __name__ == '__main__':
    np_argmax()
    # assign_val()
    # n_dimension_arr()
    # single_idx()
    # multidimen_idx()
    pass
