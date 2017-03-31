# _*_ coding:utf-8 _*_
"""
This file is about linear algebra operator
"""
import numpy as np


def mean():
    arr = np.arange(12).reshape((4, 3))
    print arr
    mean_arr = np.mean(arr, axis=0)
    print mean_arr
    print arr - mean_arr


def covariance():
    arr = np.arange(12).reshape((4, 3))
    print arr
    mean_arr = np.mean(arr, axis=0)
    print mean_arr
    cov_arr = np.cov(mean_arr, rowvar=0)
    print cov_arr
    mean_sub_arr = arr - mean_arr
    print mean_sub_arr
    print np.cov(mean_sub_arr, rowvar=0)
    print np.var(mean_sub_arr, 0)

    a = np.array([[1, 2], [3, 4]])
    print np.var(a)
    # 1.25 get variance of all the element_wise
    print np.var(a, 0)
    # [ 1.  1.] get variance of every column
    print np.var(a, 1)
    # [ 0.25  0.25] get variance of every row


if __name__ == '__main__':
    # mean()
    covariance()
    pass
