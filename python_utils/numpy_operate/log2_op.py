# coding:utf-8

import numpy as np


def log2_test():
    arr = np.array([0, 1, 2, 3, 2 ** 4])
    print np.log2(arr)
    # [-inf, 0, 1, 1.5849625, 4]

    arr = np.array([1, 2, 4, 2 ** 3])
    arr_lg = np.log2(arr)
    print arr_lg
    # [ 0.  1.  2.  3.]
    print arr_lg * arr
    # [  0.   2.   8.  24.]

    # calculate entropy
    print np.sum(arr_lg * arr)
    # 34


def cal_entropy():
    arr1 = np.array([0.5, 0.5])
    print np.log2(arr1)
    # [-1. -1.]

    print np.sum(np.log2(arr1) * arr1)
    # -1.0

    print np.sum(-1 * np.log2(arr1) * arr1)
    # 1.0

    arr2 = np.array([0.1, 0.9])
    print np.sum(-1 * np.log2(arr2) * arr2)
    # 0.468995593589

if __name__ == '__main__':
    # log2_test()
    cal_entropy()
    pass
