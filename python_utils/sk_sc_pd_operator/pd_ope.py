# coding:utf-8

import numpy as np
import pandas as pd


def idx_align_series():
    A = pd.Series([2, 4, 6], index=[0, 1, 2])
    B = pd.Series([1, 3, 5], index=[1, 2, 3])

    print A + B
    # 0    NaN
    # 1    5.0
    # 2    9.0
    # 3    NaN
    # dtype: float64

    print A.add(B, fill_value=0)
    # 0    2.0
    # 1    5.0
    # 2    9.0
    # 3    5.0
    # dtype: float64


def idx_align_df():
    rng = np.random.RandomState(42)
    df1 = pd.DataFrame(rng.randint(0, 20, (2, 2)),
                       columns=list('AB'))
    print df1
    #     A   B
    # 0   6  19
    # 1  14  10
    df2 = pd.DataFrame(rng.randint(0, 10, (3, 3)),
                       columns=list('BAC'))

    print df2
    #    B  A  C
    # 0  7  4  6
    # 1  9  2  6
    # 2  7  4  3

    print df1 + df2
    #     A     B   C
    # 0  10.0  26.0 NaN
    # 1  16.0  19.0 NaN
    # 2   NaN   NaN NaN

    fill = df1.stack().mean()
    print fill
    # 12.25
    print df1.add(df2, fill_value=fill)
    #        A      B      C
    # 0  10.00  26.00  18.25
    # 1  16.00  19.00  18.25
    # 2  16.25  19.25  15.25

    print df1
    #     A   B
    # 0   6  19
    # 1  14  10


def row_col_ope():
    rng = np.random.RandomState(42)
    arr = rng.randint(10, size=(3, 4))
    print arr
    # [[6 3 7 4]
    #  [6 9 2 6]
    # [7 4 3 7]]
    print arr - arr[0]
    # [[ 0  0  0  0]
    #  [ 0  6 -5  2]
    # [ 1  1 -4  3]]
    df = pd.DataFrame(arr, columns=list('QRST'))
    print df - df.iloc[0]
    #    Q  R  S  T
    # 0  0  0  0  0
    # 1  0  6 -5  2
    # 2  1  1 -4  3
    print df.subtract(df['R'], axis=0)
    #    Q  R  S  T
    # 0  3  0  4  1
    # 1 -3  0 -7 -3
    # 2  3  0 -1  3

    print df  # no change

if __name__ == '__main__':
    row_col_ope()
    # idx_align_df()
    # idx_align_series()
    pass
