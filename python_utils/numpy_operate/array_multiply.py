# _*_ coding:utf-8 _*_

"""
This file is some demo about numpy array multiply operator
"""
import numpy as np


def one_dim_arr_multiply():
    """
    the difference between * and dot operator about numpy.array()
    of one dimension
    :return none:
    """
    arr1 = np.array([1, 2])
    arr2 = np.array([3, 4])
    print arr1 * arr2  # -> [3 8]
    # for 1 dim array np.dot gets inner product of vector
    print np.dot(arr1, arr2.transpose())  # 11
    print arr1, arr2.transpose()
    print np.dot(arr1, arr2)  # 11


def mul_dim_arr_multiply():
    """
    the difference between * and dot operator about numpy.array()
    of multiple dimension
    """
    arr1 = np.array([[1], [2]])
    arr2 = np.array([[3], [4]])
    print arr1 * arr2
    # >> [[3]
    #     [8]]
    print np.dot(arr1, arr2.transpose())
    # >>>[[3 4]
    #     [6 8]]
    print np.dot(arr1, arr2)
    # ValueError: shapes (2,1) and (2,1) not aligned: 1 (dim 1) != 2 (dim 0)

if __name__ == '__main__':
    # one_dim_arr_multiply()
    mul_dim_arr_multiply()
