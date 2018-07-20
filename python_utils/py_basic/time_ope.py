# _*_ coding:utf-8 _*_

"""
get the seconds since epoch from the time + date output
function time consume
https://stackoverflow.com/questions/5478351/python-time-measure-function
"""

import time
import timeit


def test_time_consume():
    start = time.clock()
    time.sleep(1)
    print time.clock() - start
    # 0.999735009203


def timing(f):
    def wrap(*args):
        start = time.time()
        ret = f(*args)
        end = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (end - start) * 1000.0)
        return ret
    return wrap


@timing
def test_time():
    time.sleep(1.1)
    # test_time function took 1101.000 ms


def timeit_test():
    timeit.timeit()


def sleep_milliseconds(mi_sec=50):

    time.sleep(mi_sec / 1000.0)


@timing
def test_sp_mi_sec():
    sleep_milliseconds()


def test_time_transform():
    # time_stamp = int(time.time())
    # s = '123'
    # print time_stamp
    # # 1509953402
    # print "%s_%s.pcm" % (s, time_stamp)
    # # 123_1509953402.pcm
    # s += str(time_stamp)
    # print s

    # print time.ctime(time_stamp)
    # Thu Jun 28 07:58:58 2018
    print time.strftime("%Y-%m-%d %H:%M:%S")
    # 2018-06-28 08:00:35

    # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1509953402))
    # # 2017-11-06 15:30:02
    #
    # time_stamp = int(time.time())
    # print time_stamp
    # print divmod(time_stamp, 3600)


def str_time():
    import datetime
    str_time = '2018-02-01 0:0:0'
    d = datetime.datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    print d, d.strftime("%Y-%m-%d %H:%M:%S")
    # 2018-02-01 00:00:00, 2018-02-01 00:00:00

    for i in xrange(2):
        print d, d + datetime.timedelta(minutes=30)
        d = d + datetime.timedelta(minutes=30)

    # 2018-02-01 00:00:00 2018-02-01 00:30:00
    # 2018-02-01 00:30:00 2018-02-01 01:00:00


if __name__ == '__main__':
    # import datetime
    # str_time = '2018-03-08T08:00:00.000'
    # d = datetime.datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%S.%f")
    # print d
    # 2018-03-08 08:00:00

    import time
    str_time = '2018-03-08T08:00:00.000'
    # str_time.replace('T', ' ')

    # d = time.strftime("%Y-%m-%d %H:%M:%S.%f")

    import time

    str_time = '2018-03-08T08:00:00.000'
    d = time.strptime(str_time, "%Y-%m-%dT%H:%M:%S.%f")

    print d
    # time.struct_time(tm_year=2018, tm_mon=3, tm_mday=8, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=67, tm_isdst=-1)

    print time.strftime("%Y-%m-%d %H:%M:%S", d)
    # 2018-03-08 08:00:00

    # str_time()
    # test_time_consume()
    # test_time()
    # test_sp_mi_sec()
    # test_time_transform()
    pass
