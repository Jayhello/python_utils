# _*_ coding:utf-8 _*_

"""

"""
import numpy as np


def euclidean_distance():
    a1 = np.array([1, 2, 3])
    a2 = np.array([3, 4, 5])
    print np.square(a1, a2)


def np_sum():
    a1 = np.array([1, 2, 3])
    a2 = np.array([3, 4, 5])
    print a1 - a2
    # [-2 -2 -2]
    print (a1 - a2)**2
    # [4 4 4]
    print np.sum(a1 - a2)
    # -6
    print np.sum((a1 - a2)**2)
    # 12


def np_sqrt():
    a1 = np.array([1, 4, 9])
    print np.sqrt(a1)
    # [ 1.  2.  3.]


def euclidean_distance_v2():
    a1 = np.array([1, 2, 3])
    a2 = np.array([3, 4, 5])
    print np.sqrt(np.sum((a1 - a2)**2))
    # 3.46410161514


def euclidean_distance_v3():
    a1 = np.array([1, 2, 3])
    a2 = np.array([3, 4, 5])
    print np.linalg.norm(a1 - a2)
    # 3.46410161514


def eu_distance():
    a1 = [1, 2, 3]
    a2 = [3, 4, 5]
    from math import sqrt
    print sqrt(sum((a - b)**2 for a, b in zip(a1, a2)))
    # 3.46410161514

if __name__ == '__main__':
    euclidean_distance()
    # euclidean_distance_v2()
    # np_sum()
    # euclidean_distance_v3()
    # np_sqrt()
    pass
