# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def factorize_1():
    df = pd.DataFrame({"A": list('cbaa'),
                       "B": list('zyxz')})

    print df
    #    A  B
    # 0  c  z
    # 1  b  y
    # 2  a  x
    # 3  a  z

    print df.apply(lambda col: pd.factorize(col, sort=True)[0])
    #    A  B
    # 0  2  2
    # 1  1  1
    # 2  0  0
    # 3  0  2

    print df.apply(lambda col: pd.factorize(col)[0])
    #    A  B
    # 0  0  0
    # 1  1  1
    # 2  2  2
    # 3  2  0


def count_1():
    df = pd.DataFrame({'a': list('absba')})
    print df.groupby('a')['a'].count()
    #      a
    # a    2
    # b    2
    # s    1

    print df['a'].value_counts()
    # b    2
    # a    2
    # s    1
    df['freq'] = df.groupby('a')['a'].transform('count')
    print df
    #    a  freq
    # 0  a     2
    # 1  b     2
    # 2  s     1
    # 3  b     2
    # 4  a     2

if __name__ == '__main__':
    count_1()
    # factorize_1()
    pass
