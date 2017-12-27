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


def rename_columns():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    print df
    #    A  B  C
    # 0  1  4  7
    # 1  2  5  8
    # 2  3  6  9

    # df = df.rename(columns={"A": "a"}, inplace=True)
    df.rename(columns={"B": "b"}, inplace=True)
    print df
    #    A  b  C
    # 0  1  4  7
    # 1  2  5  8
    # 2  3  6  9

    df.columns = list('abc')

    print df
    #    a  b  c
    # 0  1  4  7
    # 1  2  5  8
    # 2  3  6  9

    df.columns.values[2] = 'C'
    print df
    # a  b  C
    # 0  1  4  7
    # 1  2  5  8
    # 2  3  6  9

if __name__ == '__main__':
    rename_columns()
    # test_index_2()
    # test_index_1()
    pass
