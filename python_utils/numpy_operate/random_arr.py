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
    # [ 5.5  2.5  2.5  1.   4.   4.5  5.5  3. ]
    print np.random.randint(12, size=(3, 4))
    # [[0 7 1 8]
    #  [7 1 1 2]
    #  [8 4 9 3]]


def sample_rows():
    arr1 = np.random.randint(5, size=(5, 3))
    print arr1
    # [[0 0 2]
    #  [1 2 0]
    #  [0 0 4]
    #  [3 3 4]
    #  [4 3 2]]

    print arr1[[1, 2]]
    # [[1 2 0]
    #  [0 0 4]]

    idx = np.random.randint(5, size=2)
    print idx
    # [1 2]
    print arr1[idx, :]
    # [[1 2 0]
    #  [0 0 4]]
    print arr1[idx, ]
    # [[1 2 0]
    #  [0 0 4]]

    print arr1[np.random.randint(arr1.shape[0], size=2), :]
    # [[0 0 2]
    #  [4 3 2]]


def choice_arr():
    """
    numpy.random.choice(a, size=None, replace=True, p=None)
    Generates a random sample from a given 1-D array
    a : 1-D array-like or int
    If an ndarray, a random sample is generated from its elements.
    If an int, the random sample is generated as if a were np.arange(a)
    """
    arr1 = np.arange(5)
    print arr1
    # [0 1 2 3 4]
    print np.random.choice(arr1, 2)
    # [4 0]
    print np.random.choice(5, 2)
    # [3 0]


def ran_seed():
    sd = 3
    np.random.seed(sd)
    print np.random.rand(4)
    # [ 0.5507979   0.70814782  0.29090474  0.51082761]
    print np.random.rand(4)
    # [ 0.89294695  0.89629309  0.12558531  0.20724288]

    np.random.seed(sd)
    print np.random.rand(4)
    # [ 0.5507979   0.70814782  0.29090474  0.51082761]

    np.random.seed(sd)
    arr = np.random.randint(5, size=(2, 3))
    print arr
    # [[2 0 1]
    #  [3 0 0]]
    arr = np.random.randint(5, size=(2, 3))
    print arr
    # [[0 3 2]
    #  [3 1 1]]
    np.random.seed(sd)
    arr = np.random.randint(5, size=(2, 3))
    print arr
    # [[2 0 1]
    #  [3 0 0]]

if __name__ == '__main__':
    ran_seed()
    # choice_arr()
    # print generate_random_2d_arr(4, 3)
    # random_arr()
    # random_int_arr()

    pass
