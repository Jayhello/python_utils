# _*_ coding:utf-8 _*_

"""
This file is about ways to create different types of np.array(),
like identity, diagonal matrix and so on.
"""

import numpy as np


def common_create():
    """
    common way of creating array
    :return: none
    """
    arr1 = np.array([1, 2])
    print arr1
    # [1 2]
    print arr1.shape
    # (2L,)
    arr2 = np.array([[1, 2], [3.1, 4.]])
    print arr2
    # [[ 1.   2. ]
    #  [ 3.1  4. ]]
    print arr2.shape
    # (2L, 2L)
    arr3 = np.array([[1, 2], [3, 4]], dtype=complex)
    print arr3
    # [[ 1.+0.j  2.+0.j]
    #  [ 3.+0.j  4.+0.j]]


def about_shape():
    print np.array([[1, 2, 3], [3, 4, 5]]).shape
    # (2L, 3L)
    print np.array([[1, 2, 3]]).shape
    # (1L, 3L)
    print np.array([1, 2, 3]).shape
    # (3L,)
    arr1 = np.array([[1, 2, 3], [3, 4, 5]])
    arr2 = np.array([1, 2, 3])
    print arr1 * arr2
    # [[ 1  4  9]
    #    [ 3  8 15]]
    # arr22 = np.array([[1], [2], [3]])
    # print arr1 * arr22

    print np.dot(arr1, arr2)
    # [14 26]


def broadcast_demo():
    arr = np.ones((3, 4))
    print arr
    print arr + 1

    b = np.broadcast(arr, 1)
    print b.shape
    # (3L, 4L)


def about_reshape():
    arr = np.array([[1, 2, 3], [4, 5, 6], [10, 11, 12], [13, 14, 15]])
    print arr.reshape(2, 6)
    # [[ 1  2  3  4  5  6]
    #  [10 11 12 13 14 15]]
    b = np.arange(1, 13).reshape((2, 2, 3))
    print b
    # [[[ 1  2  3]
    #   [ 4  5  6]]
    #
    #  [[ 7  8  9]
    #   [10 11 12]]]
    print b.reshape((2, 6))
    # [[ 1  2  3  4  5  6]
    #  [ 7  8  9 10 11 12]]


def lst_2_array():
    """
    list, tuple to array
    :return: none
    """
    tp = (1, 2, 3)
    lst = [[1, 2], [3, 4]]
    print np.array(lst).shape
    # (2L, 2L)
    print np.array(lst)
    # [[1 2]
    #   [3 4]]
    print np.asarray(lst)
    # [[1 2]
    #   [3 4]]
    print np.asarray(tp)
    # [1 2 3]


def file_2np_arr():
    """txt file to numpy array"""
    data_path = '../machine_learn/dataset/perception/dataset.txt'
    x = np.loadtxt(data_path, dtype=float)
    print x
    # [ [ 1.1   2.2   0]
    #   [ 3.5   3.6   1]]

if __name__ == '__main__':
    file_2np_arr()
    # broadcast_demo()
    # about_shape()
    # common_create()
    # lst_2_array()
    # about_reshape()
    lst = [[1.1, 2.3, 3], [3, 4, 5]]
    arr = np.array(lst)
    print arr[1, :]
    # [ 3.  4.  5.]
    print arr[1]
    # [ 3.  4.  5.]
    # print arr[...]

    a = np.array([[1.1, 2.3, 3]])
    print a[0].tolist()
    # print "".join([str(i) + "-" for i in a[0].tolist()])
    # 1.1-2.3-3.0-
    # if 4 in [1, 3, 5]:
    #     print 'in it'
    # print arr[0, 1], arr[0, 1].flatten.A[0]
    # print np.array(lst)[:-1]
    pass
