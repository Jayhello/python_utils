# coding: utf-8

import numpy as np
import pandas as pd


def series_demo():
    rng = np.random.RandomState(42)
    ser = pd.Series(rng.rand(5))
    print ser
    # 0    0.374540
    # 1    0.950714
    # 2    0.731994
    # 3    0.598658
    # 4    0.156019
    # dtype: float64

    print ser.sum()
    # 2.8119
    print ser.mean()
    # 0.5623


def df_demo():
    rng = np.random.RandomState(42)
    df = pd.DataFrame({'A': rng.rand(5),
                       'B': rng.rand(5)})

    print df
    #           A         B
    # 0  0.374540  0.155995
    # 1  0.950714  0.058084
    # 2  0.731994  0.866176
    # 3  0.598658  0.601115
    # 4  0.156019  0.708073
    print df.mean()
    # A    0.562385
    # B    0.477888
    # dtype: float64
    print df.mean(axis='columns')
    # 0    0.265267
    # 1    0.504399
    # 2    0.799085
    # 3    0.599887
    # 4    0.432046
    # dtype: float64


def group_by_1():
    df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                       'data': range(6)}, columns=['key', 'data'])

    print df
    #   key  data
    # 0   A     0
    # 1   B     1
    # 2   C     2
    # 3   A     3
    # 4   B     4
    # 5   C     5
    print df.groupby('key').sum()
    # key
    # A       3
    # B       5
    # C       7


def filter_func(x):
    return x['data2'].std() > 4


def agg_filter_trans_apply():
    rng = np.random.RandomState(0)
    df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                       'data1': range(6),
                       'data2': rng.randint(0, 10, 6)},
                      columns=['key', 'data1', 'data2'])

    print df
    #   key  data1  data2
    # 0   A      0      5
    # 1   B      1      0
    # 2   C      2      3
    # 3   A      3      3
    # 4   B      4      7
    # 5   C      5      9

    print df.groupby('key').aggregate(['min', np.median, max])
    #      data1            data2
    #       min median max   min median max
    # key
    # A       0    1.5   3     3    4.0   5
    # B       1    2.5   4     0    3.5   7
    # C       2    3.5   5     3    6.0   9

    print df.groupby('key').aggregate({'data1': 'min',
                                       'data2': 'max'})
    #      data1  data2
    # key
    # A        0      5
    # B        1      7
    # C        2      9

    print df.groupby('key').std()
    #        data1     data2
    # key
    # A    2.12132  1.414214
    # B    2.12132  4.949747
    # C    2.12132  4.242641
    print df.groupby('key').filter(filter_func)
    #    key  data1  data2
    # 1   B      1      0
    # 2   C      2      3
    # 4   B      4      7
    # 5   C      5      9

    print df.groupby('key').transform(lambda x: x - x.mean())
    #    data1  data2
    # 0   -1.5    1.0
    # 1   -1.5   -3.5
    # 2   -1.5   -3.0
    # 3    1.5   -1.0
    # 4    1.5    3.5
    # 5    1.5    3.0


def norm_by_data2(x):
    # x is a DataFrame of group values
    x['data1'] /= x['data2'].sum()
    return x


def apply_1():
    rng = np.random.RandomState(0)
    df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                       'data1': range(6),
                       'data2': rng.randint(0, 10, 6)},
                      columns=['key', 'data1', 'data2'])
    print df
    #   key  data1  data2
    # 0   A      0      5
    # 1   B      1      0
    # 2   C      2      3
    # 3   A      3      3
    # 4   B      4      7
    # 5   C      5      9

    print df.groupby('key').apply(norm_by_data2)
    #   key     data1  data2
    # 0   A  0.000000      5
    # 1   B  0.142857      0
    # 2   C  0.166667      3
    # 3   A  0.375000      3
    # 4   B  0.571429      7
    # 5   C  0.416667      9


def apply_normalize():
    rng = np.random.RandomState(0)
    df = pd.DataFrame({'key': ['A', 'B', 'C', 'A'],
                       'data1': range(1, 5),
                       'data2': rng.randint(0, 10, 4)},
                      columns=['key', 'data1', 'data2'])

    print df
    #    key  data1  data2
    # 0   A      0      5
    # 1   B      1      0
    # 2   C      2      3
    # 3   A      3      3

    cols_to_norm = ['data1']
    f_norm = lambda x: (x - x.min()) / (x.max() - x.min())
    df[cols_to_norm] = df[cols_to_norm].apply(f_norm)

    print df
    #   key     data1  data2
    # 0   A  0.000000      5
    # 1   B  0.333333      0
    # 2   C  0.666667      3
    # 3   A  1.000000      3


def apply_norm_all():
    rng = np.random.RandomState(0)
    df = pd.DataFrame({'data1': range(1, 5),
                       'data2': rng.randint(0, 10, 4)},
                      columns=['data1', 'data2'])
    print df
    #    data1  data2
    # 0      1      5
    # 1      2      0
    # 2      3      3
    # 3      4      3

    fun = lambda x: x / x.max()
    df = df.apply(fun)
    print df
    #    data1  data2
    # 0   0.25    1.0
    # 1   0.50    0.0
    # 2   0.75    0.6
    # 3   1.00    0.6

if __name__ == '__main__':
    apply_norm_all()
    # apply_normalize()
    # apply_1()
    # agg_filter_trans_apply()
    # group_by_1()
    # df_demo()
    # series_demo()
    pass
