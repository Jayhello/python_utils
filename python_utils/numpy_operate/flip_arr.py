# _*_ coding:utf-8 _*_

import numpy as np


def flip_arr():
    arr = np.arange(6).reshape(2, 3)
    print arr
    # [[0 1 2]
    #  [3 4 5]]
    print np.fliplr(arr)
    # [[2 1 0]
    #  [5 4 3]]
    print arr[:, ::-1]
    # [[2 1 0]
    #  [5 4 3]]

    print np.flipud(arr)
    # [[3 4 5]
    #  [0 1 2]]
    print arr[::-1]
    # [[3 4 5]
    #  [0 1 2]]

    arr2 = np.arange(8).reshape((2, 2, 2))
    print arr2
    # [[[0 1]
    #   [2 3]]
    #
    # [[4 5]
    # [6 7]]]


if __name__ == '__main__':
    flip_arr()
    pass
