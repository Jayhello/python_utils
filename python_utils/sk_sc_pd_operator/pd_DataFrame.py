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


def df_multi_idx_1():
    df = pd.DataFrame(np.random.rand(4, 2),
                      index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                      columns=['data1', 'data2'])

    print df
    #      data1     data2
    # a 1  0.737537  0.102676
    #   2  0.755261  0.715244
    # b 1  0.411588  0.081071
    #   2  0.915185  0.982820


def df_feature_name():
    lst = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
    df = pd.DataFrame(lst)
    print df
    #      a  b    c
    # 0  1.0  2  NaN
    # 1  NaN  3  4.0

    print df.columns
    # Index([u'a', u'b', u'c'], dtype='object')

    print list(df.columns.values)
    print df.columns.tolist()
    print list(df)
    # above three are the same ['a', 'b', 'c']


def df_to_csv():
    js_data = {"data": [{"uid":"1080427621","sid":"1330761808","ssid":"1330761808","asid":"","title":"我来卖玉","cover":"https://screenshot.dwstatic.com/yjmf/1080427621_1496652244.682569.jpg?imageview/4/0/w/363/h/330/exif/0/blur/1.0","count":"4","yyno":"1148665362","nickname":"逝水","start_time":"1498493654000","is_living":"0","tag_type":0},
                        {"uid":"1080427621","sid":"1330761808","ssid":"1330761808","asid":"","title":"我来卖玉","cover":"https://screenshot.dwstatic.com/yjmf/1080427621_1496652244.682569.jpg?imageview/4/0/w/363/h/330/exif/0/blur/1.0","count":"4","yyno":"1148665362","nickname":"逝水","start_time":"1498493654000","is_living":"0","tag_type":0}]}

    # js_data = {"data": [{'start_time': 1476329529}, {'start_time': 1476329529}]}
    # df = pd.DataFrame(js_data['data'])
    # df['start_time'] = pd.to_datetime(df['start_time'], unit='s')
    # df['start_time'] = df['start_time'].apply(int)
    # print pd.to_datetime(df['start_time'], unit='s')

    df = pd.DataFrame(js_data['data'])
    print df.head()

    path = 'E:/baiduyun_voice/codec_inneed/yi_jian_app.csv'
    # df.to_csv(path, index=False, encoding='gb2312')
    df.to_csv(path, index=False)

if __name__ == '__main__':
    df_to_csv()
    # df_feature_name()
    # df_multi_idx_1()
    # test_df_idx_3()
    # test_df_idx_2()
    # test_data_frame_4()
    # test_data_frame_3()
    # test_data_frame_2()
    # test_data_frame_1()
    pass
