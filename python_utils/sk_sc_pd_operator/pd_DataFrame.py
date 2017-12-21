# coding:utf-8

import pandas as pd
import numpy as np


def test_data_frame_1():
    data = [{'a': i, 'b': i * 2} for i in xrange(1, 4)]
    print data
    # [{'a': 1, 'b': 2}, {'a': 2, 'b': 4}, {'a': 3, 'b': 6}]
    df = pd.DataFrame(data)
    print df
    #    a  b
    # 0  1  2
    # 1  2  4
    # 2  3  6

    print df['b']
    # 0    2
    # 1    4
    # 2    6
    # Name: b, dtype: int64


def test_data_frame_2():
    d_population = {'bj': 3000, 'sh': 2500, 'gz': 3000, 'sz': 2000}
    d_area = {'bj': 30, 'sh': 25, 'gz': 30, 'sz': 20}

    states = pd.DataFrame({'population': d_population,
                           'area': d_area})

    print states
    #     area  population
    # bj    30        3000
    # gz    30        3000
    # sh    25        2500
    # sz    20        2000

    print states.index
    # Index([u'bj', u'gz', u'sh', u'sz'], dtype='object')
    print states.columns
    # Index([u'area', u'population'], dtype='object')

    s_p = pd.Series(d_population)
    s_a = pd.Series(d_area)
    # equivalent to the above
    print pd.DataFrame({'population': s_p,
                        'area': s_a})


def test_data_frame_3():
    lst = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
    print pd.DataFrame(lst)
    #      a  b    c
    # 0  1.0  2  NaN
    # 1  NaN  3  4.0


def test_data_frame_4():
    df = pd.DataFrame(np.arange(6).reshape(3, 2),
                      columns=['even', 'odd'],
                      index=['a', 'b', 'c'])

    print df
    #    even  odd
    # a     0    1
    # b     2    3
    # c     4    5


def test_df_idx_1():
    d_population = {'bj': 3000, 'sh': 2500, 'gz': 3000, 'sz': 2000}
    d_area = {'bj': 30, 'sh': 25, 'gz': 30, 'sz': 20}

    data = pd.DataFrame({'pop': d_population, 'area': d_area})

    print data['area']
    # bj    30
    # gz    30
    # sh    25
    # sz    20
    # Name: area, dtype: int64

    # print data['gz'] KeyError: 'gz'

    print data.area  # equivalent to the above data['area']

    print data.area is data['area']  # True

    data['density'] = data['pop'] / data['area']

    print data
    #     area   pop  density
    # bj    30  3000    100.0
    # gz    30  3000    100.0
    # sh    25  2500    100.0
    # sz    20  2000    100.0

    # raw underlying data array
    print data.values
    # [[   30.  3000.   100.]
    #  [   30.  3000.   100.]
    #  [   25.  2500.   100.]
    #  [   20.  2000.   100.]]

    # accesses a row
    print data.values[0]
    # [   30.  3000.   100.]

    print data.T
    #              bj      gz      sh      sz
    # area       30.0    30.0    25.0    20.0
    # pop      3000.0  3000.0  2500.0  2000.0
    # density   100.0   100.0   100.0   100.0


def test_df_idx_2():
    d_population = {'bj': 3000, 'sh': 2500, 'gz': 3000, 'sz': 2000}
    d_area = {'bj': 30, 'sh': 25, 'gz': 30, 'sz': 20}

    data = pd.DataFrame({'pop': d_population, 'area': d_area})
    data['density'] = data['pop'] / data['area']

    print data
    #     area   pop  density
    # bj    30  3000    100.0
    # gz    30  3000    100.0
    # sh    25  2500    100.0
    # sz    20  2000    100.0

    print data.iloc[1:3, 1:3]
    #      pop  density
    # gz  3000    100.0
    # sh  2500    100.0

    print data.iloc[0, :]
    # area         30.0
    # pop        3000.0
    # density     100.0
    # Name: bj, dtype: float64

    print data.loc['gz':'sh', 'pop':'density']
    #     pop   density
    # gz  3000    100.0
    # sh  2500    100.0

    print data.loc[data.area > 25, ['area', 'density']]
    #     area  density
    # bj    30    100.0
    # gz    30    100.0

    print data.ix[:2, :'pop']
    #     area   pop
    # bj    30  3000
    # gz    30  3000

    print data.ix[:1, :'density']
    #     area   pop  density
    # bj    30  3000    100.0

    data.iloc[0, 2] = 9999
    print data
    #     area   pop  density
    # bj    30  3000   9999.0
    # gz    30  3000    100.0
    # sh    25  2500    100.0
    # sz    20  2000    100.0


def test_df_idx_3():
    d_population = {'bj': 3000, 'sh': 2500, 'gz': 3000, 'sz': 2000}
    d_area = {'bj': 30, 'sh': 25, 'gz': 30, 'sz': 20}

    data = pd.DataFrame({'pop': d_population, 'area': d_area})
    data['density'] = data['pop'] / data['area']

    print data
    #     area   pop  density
    # bj    30  3000    100.0
    # gz    30  3000    100.0
    # sh    25  2500    100.0
    # sz    20  2000    100.0

    print data['bj': 'gz']  # can't use data['bj']
    #     area   pop  density
    # bj    30  3000    100.0
    # gz    30  3000    100.0

    print data['bj': 'bj']
    #     area   pop  density
    # bj    30  3000    100.0

    print data[1: 2]
    #     area   pop  density
    # gz    30  3000    100.0

    print data[data.area < 25]
    #     area   pop  density
    # sz    20  2000    100.0

if __name__ == '__main__':
    test_df_idx_3()
    # test_df_idx_2()
    # test_data_frame_4()
    # test_data_frame_3()
    # test_data_frame_2()
    # test_data_frame_1()
    pass
