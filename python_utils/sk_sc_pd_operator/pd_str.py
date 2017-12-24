# coding:utf-8

import numpy as np
import pandas as pd


def series_str():
    data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
    names = pd.Series(data)
    print names.str.capitalize()
    # 0    Peter
    # 1     Paul
    # 2     None
    # 3     Mary
    # 4    Guido
    # dtype: object

    print names.str.startswith('p')
    # 0     True
    # 1    False
    # 2     None
    # 3    False
    # 4    False
    # dtype: object

if __name__ == '__main__':
    series_str()
    pass
