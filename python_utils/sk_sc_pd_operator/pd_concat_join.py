# coding:utf-8

import numpy as np
import pandas as pd


def np_arr_concat():
    x = [1, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]

    print np.concatenate([x, y, z])
    # [1 2 3 4 5 6 7 8 9]

    x = [[1, 2],
         [3, 4]]
    print np.concatenate([x, x])
    # [[1 2]
    #  [3 4]
    #  [1 2]
    #  [3 4]]

    print np.concatenate([x, x], axis=1)
    # [[1 2 1 2]
    #  [3 4 3 4]]


def make_df(cols, idx):
    """
    make_df('ABC', range(3))
    cols->ABC, idx -> [0, 1, 2]
    return
       A  B  C
    0 A0 B0 C0
    1 A1 B1 C1
    2 A2 B2 C2
    """
    data = {c:[str(c) + str(i) for i in idx] for c in cols}

    return pd.DataFrame(data, idx)


def series_concat():
    ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
    ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
    print pd.concat([ser1, ser2])
    # 1    A
    # 2    B
    # 3    C
    # 4    D
    # 5    E
    # 6    F
    # dtype: object


def df_concat():
    df1 = make_df('AB', [1, 2])
    df2 = make_df('AB', [3, 4])
    print df1
    #     A   B
    # 1  A1  B1
    # 2  A2  B2
    print df2
    #     A   B
    # 3  A3  B3
    # 4  A4  B4
    print pd.concat([df1, df2])
    #     A   B
    # 1  A1  B1
    # 2  A2  B2
    # 3  A3  B3
    # 4  A4  B4

    df3 = make_df('AB', [0, 1])
    df4 = make_df('CD', [0, 1])

    print df3
    #     A   B
    # 0  A0  B0
    # 1  A1  B1
    print df4
    #     C   D
    # 0  C0  D0
    # 1  C1  D1
    print pd.concat([df3, df4], axis=1)
    #     A   B   C   D
    # 0  A0  B0  C0  D0
    # 1  A1  B1  C1  D1

if __name__ == '__main__':
    df_concat()
    # series_concat()
    # np_arr_concat()
    pass
