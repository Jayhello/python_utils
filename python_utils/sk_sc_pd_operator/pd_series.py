# coding:utf-8

import numpy as np
import pandas as pd


def test_series_1():
    data = pd.Series([0.25, 0.5, 0.75, 1])
    print data
    # 0    0.25
    # 1    0.50
    # 2    0.75
    # 3    1.00
    # dtype: float64
    print data.values
    # [ 0.25  0.5   0.75  1.  ]
    print data.index
    # RangeIndex(start=0, stop=4, step=1)
    print data[1:3]
    # 1    0.50
    # 2    0.75
    # dtype: float64


def test_series_2():
    data = pd.Series([0.2, 0.4, 0.6], index=['a', 'b', 'c'])
    print data
    # a    0.2
    # b    0.4
    # c    0.6
    # dtype: float64

    print data['b']  # 0.4
    print data[0:2]
    # a    0.2
    # b    0.4
    # dtype: float64

    data = pd.Series([0.25, 0.5, 0.75, 1.0],
                     index=[2, 5, 3, 7])


def test_series_3():
    d_population = {'bj': 3000, 'sh': 2500, 'gz': 3000, 'sz': 2000}
    population = pd.Series(d_population)
    print population
    # bj    3000
    # gz    3000
    # sh    2500
    # sz    2000
    # dtype: int64

    print population['bj']   # 3000

    print population['sh': 'sz']
    # sh    2500
    # sz    2000
    # dtype: int64

    print pd.Series({2: 'a', 1: 'b', 3: 'c'}, index=[3, 2])
    # 3    c
    # 2    a
    # dtype: object


def series_idx_1():
    lst = np.linspace(0.25, 1, 4)
    print lst
    # [ 0.25  0.5   0.75  1.  ]
    data = pd.Series(lst, index=['a', 'b', 'c', 'd'])

    print data
    # a    0.25
    # b    0.50
    # c    0.75
    # d    1.00
    # dtype: float64
    print data['b']  # 0.5

    print 'a' in data  # True

    print data.keys()
    # Index([u'a', u'b', u'c', u'd'], dtype='object')
    print data.values
    # [ 0.25  0.5   0.75  1.  ]
    print data.tolist()
    # [0.25, 0.5, 0.75, 1.0]
    # add 'e' to data
    data['e'] = 1.25
    print data
    # a    0.25
    # b    0.50
    # c    0.75
    # d    1.00
    # e    1.25
    # dtype: float64


def series_idx_2():
    lst = np.linspace(0.25, 1, 4)
    data = pd.Series(lst, index=['a', 'b', 'c', 'd'])

    print data['a': 'c']
    # a    0.25
    # b    0.50
    # c    0.75
    # dtype: float64

    print data[0: 2]
    # a    0.25
    # b    0.50
    # dtype: float64

    print data[(data > 0.3) & (data < 0.8)]
    # b    0.50
    # c    0.75
    # dtype: float64

    data['e'] = 1.25
    print data[['a', 'e']]
    # a    0.25
    # e    1.25
    # dtype: float64


def series_idx_3():
    data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
    print data
    # 1    a
    # 3    b
    # 5    c
    # dtype: object
    # explicit index when indexing
    print data[1]  # a

    # implicit index when slicing
    print data[1: 3]
    # 3    b
    # 5    c
    # dtype: object

    # explicit index
    print data.loc[1: 3]
    # 1    a
    # 3    b
    # dtype: object

    print data.loc[1]
    # a

    # implicit
    print data.iloc[1: 3]
    # 3    b
    # 5    c
    # dtype: object
    print data.iloc[1]
    # b


def series_mul_idx_1():
    city_year = [('bj', 2000), ('bj', 2010),
                 ('gz', 2000), ('gz', 2010),
                 ('sh', 2000), ('sh', 2010)]

    price = [4000, 50000, 2000, 15000, 5000, 50000]

    h_price = pd.Series(price, index=city_year)
    print h_price
    # (bj, 2000)     4000
    # (bj, 2010)    50000
    # (gz, 2000)     2000
    # (gz, 2010)    15000
    # (sh, 2000)     5000
    # (sh, 2010)    50000
    # dtype: int64

    # print year 2000 house price
    print h_price[[i for i in h_price.index if i[1] == 2000]]
    # (bj, 2000)    4000
    # (gz, 2000)    2000
    # (sh, 2000)    5000
    # dtype: int64

    # high efficient way
    idx = pd.MultiIndex.from_tuples(city_year)
    print idx
    # MultiIndex(levels=[[u'bj', u'gz', u'sh'], [2000, 2010]],
    #            labels=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]])

    h_price = h_price.reindex(idx)
    print h_price
    # bj  2000     4000
    #     2010    50000
    # gz  2000     2000
    #     2010    15000
    # sh  2000     5000
    #     2010    50000

    # print year 2000 house price
    print h_price[:, 2000]
    # bj    4000
    # gz    2000
    # sh    5000

    # convert a multiply-indexed  Series into a conventionally indexed  DataFrame
    h_prices_df = h_price.unstack()
    print h_prices_df
    #     2000   2010
    # bj  4000  50000
    # gz  2000  15000
    # sh  5000  50000

    # add lowest house price of each year
    df_h_price = pd.DataFrame({'price': h_price,
                               'price_lowest': [2000, 20000, 1500, 8000, 2500, 25000]})
    print df_h_price
    #           price         price_lowest
    # bj 2000   4000          2000
    #    2010   50000         20000
    # gz 2000   2000          1500
    #    2010   15000         8000
    # sh 2000   5000          2500
    #     2010  50000         25000

    # fraction of price_lowest/price
    f_price = df_h_price['price_lowest'] / df_h_price['price']
    print f_price.unstack()
    #     2000      2010
    # bj  0.50  0.400000
    # gz  0.75  0.533333
    # sh  0.50  0.500000

if __name__ == '__main__':
    series_mul_idx_1()
    # series_idx_3()
    # series_idx_2()
    # series_idx_1()
    # test_series_1()
    # test_series_2()
    # test_series_3()
    pass
