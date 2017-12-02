# coding:utf-8

import numpy as np


def test_unique():
    y = np.array([-1, -1, 1, 1, -1, -1, -1, 1, 1])
    unique_y = np.unique(y)
    print unique_y, unique_y.shape
    # [-1  1] (2L,)

    print np.equal(y, 1)
    # [False False  True  True False False False  True  True]
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


def test_count():
    b_arr = np.array([[0, 0, 1], [1, 0, 1], [1, 0, 1]], dtype=np.bool)
    print b_arr
    # [[False False  True]
    #  [ True False  True]
    #  [ True False  True]]
    print np.sum(b_arr)
    # 5
    print np.count_nonzero(b_arr)
    # 5

    # print len(np.where(b_arr==False))  # statistic False
    # # 2
    print np.size(b_arr)
    # 9
    print np.count_nonzero(b_arr)
    # 5
    b_lst = [True, True, True, False, False]
    print sum(b_lst)
    # 3


def test_where():
    arr = np.array([1, 2, 2, 5, 0])
    print np.where(arr==2)
    # (array([1, 2], dtype=int64),)
    print len(np.where(arr==2))
    # 1

    arr2 = np.array([[1, 2, 3], [0, 5, 2]])
    print arr2
    # [[1 2 3]
    #  [0 5 2]]

    arr2_con = np.where(arr2==2)
    print arr2_con
    # (array([0, 1], dtype=int64), array([1, 2], dtype=int64))
    print len(arr2_con), np.size(arr2_con)
    # 2, 4

    a = np.arange(5, 10)
    print a
    # [5 6 7 8 9]
    a_con = np.where(a < 8)
    print a_con, np.size(a_con)
    # (array([0, 1, 2], dtype=int64),) 3

    print a[a_con]
    # [5 6 7]

    print len(a_con)
    # 1

    a_con = np.where(a < 8)
    for item in a_con:
        print item
    # [0 1 2]

    a = np.arange(4, 10).reshape(2, 3)
    print a
    # [[4 5 6]
    #  [7 8 9]]
    print np.where(a > 7)
    # (array([1, 1], dtype=int64), array([1, 2], dtype=int64))
    print a[np.where(a > 7)]
    # [8 9]

    x = np.arange(9).reshape(3, 3)
    print x
    # [[0 1 2]
    #  [3 4 5]
    #  [6 7 8]]

    print np.where(x > 3)
    # (array([1, 1, 2, 2, 2], dtype=int64), array([1, 2, 0, 1, 2], dtype=int64))

    print x[np.where(x > 3)]
    # [4 5 6 7 8]


def test_sum():
    arr = np.arange(24).reshape((2, 3, 4))
    print arr
    # [[[ 0  1  2  3]
    #   [ 4  5  6  7]
    #   [ 8  9 10 11]]
    #
    # [[12 13 14 15]
    #  [16 17 18 19]
    #  [20 21 22 23]]]

    print arr[0, :, :]
    # [[ 0  1  2  3]
    #  [ 4  5  6  7]
    #  [ 8  9 10 11]]

    print arr[0::]  # print arr

    print arr[:, 1, :]
    # [[ 4  5  6  7]
    #  [16 17 18 19]]

    print arr[:, :, 2]
    # [[ 2  6 10]
    #  [14 18 22]]

    print arr.sum(1)
    # [[12 15 18 21]
    #  [48 51 54 57]]
    print arr[:, 0, :] + arr[:, 1, :] + arr[:, 2, :]
    # [[12 15 18 21]
    #  [48 51 54 57]]

    # arr.sum(0) => arr[0, :, :] + arr[1, :, :]
    # arr.sum(1) => arr[:, 0, :] + arr[:, 1, :] + arr[:, 2, :]
    # arr.sum(2) => arr[:, :, 0] + arr[:, :, 1] + arr[:, :, 2] + arr[:, :, 2]

if __name__ == '__main__':
    # test_unique()
    # test_count()
    # test_sum()
    test_where()
    pass
