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
    print np.mean(arr)
    print np.mean(arr, axis=1)


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


def eigen_vec_val():
    arr1 = np.array([[-1, 0], [0, 1]])
    eig_val1, eig_vec1 = np.linalg.eig(arr1)
    # print eig_val1
    # print eig_vec1

    arr2 = np.random.randint(1, 10, size=(3, 3))
    eig_val2, eig_vec2 = np.linalg.eig(arr2)
    print eig_val2
    print eig_vec2
    eig_val2_idx = np.argsort(eig_val2)
    print eig_val2_idx
    print eig_val2_idx[::-1]
    print eig_vec2[:, eig_val2_idx]
    print eig_vec2[:, eig_val2_idx[::-1]]

if __name__ == '__main__':
    # mean()
    # covariance()
    eigen_vec_val()
    pass
