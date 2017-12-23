# coding:utf-8

import numpy as np
import pandas as pd


def miss_series():
    data = pd.Series([1, np.nan, 'hello', None])

    print data.isnull()
    # 0    False
    # 1     True
    # 2    False
    # 3     True
    # dtype: bool
    print data[data.notnull()]
    # 0        1
    # 2    hello
    # dtype: object
    print data.dropna()
    # 0        1
    # 2    hello
    # dtype: object


def miss_df():
    df = pd.DataFrame([[1, np.nan, 2],
                       [2, 3, 5],
                       [np.nan, 4, 6]])

    print df
    #      0    1  2
    # 0  1.0  NaN  2
    # 1  2.0  3.0  5
    # 2  NaN  4.0  6
    print df.dropna()
    #      0    1  2
    # 1  2.0  3.0  5
    print df.dropna(axis=1)
    #    2
    # 0  2
    # 1  5
    # 2  6

    df[3] = np.nan
    print df
    #      0    1  2   3
    # 0  1.0  NaN  2 NaN
    # 1  2.0  3.0  5 NaN
    # 2  NaN  4.0  6 NaN
    print df.dropna(axis='columns', how='all')
    #      0    1  2
    # 0  1.0  NaN  2
    # 1  2.0  3.0  5
    # 2  NaN  4.0  6
    print df.dropna(axis='rows', thresh=3)
    #      0    1  2   3
    # 1  2.0  3.0  5 NaN


def fill_series():
    data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
    print data
    # a    1.0
    # b    NaN
    # c    2.0
    # d    NaN
    # e    3.0
    # dtype: float64
    data.fillna(0)
    print data
    # a    1.0
    # b    NaN
    # c    2.0
    # d    NaN
    # e    3.0
    # dtype: float64

    # We can specify a forward-fill to propagate the previous value forward:
    print data.fillna(method='ffill')
    # a    1.0
    # b    1.0
    # c    2.0
    # d    2.0
    # e    3.0
    # dtype: float64

    # Or we can specify a back-fill to propagate the next values backward:
    print data.fillna(method='bfill')
    # a    1.0
    # b    2.0
    # c    2.0
    # d    3.0
    # e    3.0
    # dtype: float64


def fill_df():
    df = pd.DataFrame([[1, np.nan, 2],
                       [2, 3, 5],
                       [np.nan, 4, 6]])

    df[3] = np.nan
    print df
    #      0    1  2   3
    # 0  1.0  NaN  2 NaN
    # 1  2.0  3.0  5 NaN
    # 2  NaN  4.0  6 NaN

    print df.fillna(method='ffill', axis=1)
    #      0    1    2    3
    # 0  1.0  1.0  2.0  2.0
    # 1  2.0  3.0  5.0  5.0
    # 2  NaN  4.0  6.0  6.0


if __name__ == '__main__':
    fill_df()
    # fill_series()
    # miss_df()
    # miss_series()
    pass
