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


if __name__ == '__main__':
    print generate_random_2d_arr(4, 3)
    pass
