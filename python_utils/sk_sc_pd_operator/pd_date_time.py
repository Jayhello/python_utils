# coding:utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
seaborn.set()


def np_dt():
    date = np.array('2017-09-28', dtype=np.datetime64)
    print date + np.arange(5)
    # ['2017-09-28' '2017-09-29' '2017-09-30' '2017-10-01' '2017-10-02']


def series_dt():
    index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                              '2015-07-04', '2015-08-04'])
    data = pd.Series([0, 1, 2, 3], index=index)
    print data
    # 2014-07-04    0
    # 2014-08-04    1
    # 2015-07-04    2
    # 2015-08-04    3
    # dtype: int64

    print data['2014-07-04':'2014-09-04']
    # 2014-07-04    0
    # 2014-08-04    1
    # dtype: int64

    print data['2015']
    # 2015-07-04    2
    # 2015-08-04    3
    # dtype: int64


def pd_time():
    from datetime import datetime
    dates = pd.to_datetime([datetime(2015, 7, 3), '4th of July, 2015',
                            '2015-Jul-6', '07-07-2015', '20150708'])

    print dates

    print dates.to_period('D')
    # PeriodIndex(['2015-07-03', '2015-07-04', '2015-07-06', '2015-07-07',
    #              '2015-07-08'],
    #             dtype='int64', freq='D')
    print dates - dates[0]
    # TimedeltaIndex(['0 days', '1 days', '3 days',
    #                  '4 days', '5 days'],
    #               dtype='timedelta64[ns]', freq=None)

    print pd.date_range('2015-07-03', '2015-07-5')
    # DatetimeIndex(['2015-07-03', '2015-07-04', '2015-07-05'],
    #               dtype='datetime64[ns]', freq='D')
    print pd.date_range('2015-07-03', periods=3)
    # as above

    print pd.date_range('2015-07-03', periods=3, freq='H')
    # DatetimeIndex(['2015-07-03 00:00:00', '2015-07-03 01:00:00',
    #                '2015-07-03 02:00:00'],
    #               dtype='datetime64[ns]', freq='H')

    print pd.period_range('2015-07', periods=3, freq='M')
    # PeriodIndex(['2015-07', '2015-08', '2015-09'],
    #               dtype='int64', freq='M')


def pd_time_offset():
    from pandas.tseries.offsets import BDay

    print pd.timedelta_range(0, periods=3, freq="2H30T")
    # TimedeltaIndex(['00:00:00', '02:30:00', '05:00:00'],
    #           dtype='timedelta64[ns]', freq='150T')
    print pd.date_range('2015-07-01', periods=3, freq=BDay())
    # DatetimeIndex(['2015-07-01', '2015-07-02', '2015-07-03'],
    #           dtype='datetime64[ns]', freq='B')


def pandas_datareader_1():
    from pandas_datareader import data
    goog = data.DataReader('GOOG', start='2004', end='2016',
                           data_source='google')

    print goog.head()

    goog = goog['Close']
    goog.plot()


if __name__ == '__main__':
    pandas_datareader_1()
    # pd_time_offset()
    # pd_time()
    # series_dt()
    # np_dt()
    pass
