# coding:utf-8

import pandas as pd


def test_index_1():
    idx = pd.Index([2, 3, 7, 5, 3])
    print idx
    # Int64Index([2, 3, 7, 5, 3], dtype='int64')
    print idx[1]
    # 3
    print idx[::2]
    # Int64Index([2, 7, 3], dtype='int64')

    print idx.size, idx.shape, idx.ndim, idx.dtype
    # 5 (5L,) 1 int64


def test_index_2():
    idx_1 = pd.Index([1, 3, 5, 7, 9])
    idx_2 = pd.Index([2, 3, 5, 7, 11])

    print idx_1 & idx_2
    # Int64Index([3, 5, 7], dtype='int64')
    print idx_1 | idx_2
    # Int64Index([1, 2, 3, 5, 7, 9, 11], dtype='int64')
    print idx_1 ^ idx_2
    # Int64Index([1, 2, 9, 11], dtype='int64')


if __name__ == '__main__':
    test_index_2()
    # test_index_1()
    pass
