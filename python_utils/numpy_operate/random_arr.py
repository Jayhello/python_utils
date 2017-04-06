# _*_ coding:utf-8 _*_

"""
This module is some example about random array
"""
import numpy as np


def generate_random_2d_arr(col, row):
    """
    generate random 2d array from 0~col*row
    :param col: the num of column
    :param row: the num of row
    :return: like generate_random_2d_arr(4, 3)
                    [[ 7 10  5]
                     [ 3  4  2]
                     [ 8 11  6]
                     [ 9  1  0]]
    """
    return np.random.permutation(col * row).reshape(row, col)


def random_arr():
    a = np.random.random(size=(2, 4))
    print a
    # [[ 0.13652737  0.32546344  0.58527282  0.0899639 ]
    #  [ 0.21190661  0.05351992  0.42603268  0.17524264]]


def random_int_arr():
    print np.random.random_integers(5)
    # like 3
    arr = np.random.random_integers(12, size=(3, 4))
    print arr
    # [[ 2  9  7  6]
    #  [ 9  1  9  1]
    #  [ 8  6 11  5]]
    d1 = np.random.random_integers(1, 6, 10)
    print d1
    # [6 4 5 2 4 1 1 5 6 2]
    arr_f = 0.5 * (np.random.random_integers(12, size=(8, )) - 1)
    print arr_f

    print np.random.randint(12, size=(3, 4))
    # [[0 7 1 8]
    #  [7 1 1 2]
    #  [8 4 9 3]]


if __name__ == '__main__':
    # print generate_random_2d_arr(4, 3)
    # random_arr()
    random_int_arr()

    pass
