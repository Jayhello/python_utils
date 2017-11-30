# coding:utf-8

import numpy as np


def test_unique():
    y = np.array([-1, -1, 1, 1, -1, -1, -1, 1, 1])
    unique_y = np.unique(y)
    print unique_y, unique_y.shape
    # [-1  1] (2L,)

    for v in unique_y:
        print np.sum(np.equal(y, v))
    # 5, 4

    print np.unique(y, return_index=True)
    # (array([-1,  1]), array([0, 2], dtype=int64))
    print np.unique(y, return_counts=True)
    # (array([-1,  1]), array([5, 4], dtype=int64))
    print np.unique(y, return_inverse=True)
    # (array([-1,  1]), array([0, 0, 1, 1, 0, 0, 0, 1, 1], dtype=int64))

    arr = np.array([1, 1, 1, 2, 2, 2, 5, 25, 1, 1])
    u_arr, counts = np.unique(arr, return_counts=True)
    print u_arr, counts
    # [ 1  2  5 25] [5 3 1 1]

    print np.asarray((u_arr, counts))
    # [[ 1  2  5 25]
    #  [ 5  3  1  1]]

    print np.asarray((u_arr, counts)).T
    # [[ 1  5]
    #  [ 2  3]
    #  [ 5  1]
    #  [25  1]]

    print np.array((u_arr, counts))
    # [[ 1  2  5 25]
    #  [ 5  3  1  1]]

    print np.bincount(arr)

if __name__ == '__main__':
    test_unique()

    pass
