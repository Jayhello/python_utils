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
    time_stamp = int(time.time())
    s = '123'
    print time_stamp
    # 1509953402
    print "%s_%s.pcm" % (s, time_stamp)
    # 123_1509953402.pcm
    s += str(time_stamp)
    print s

    print time.ctime(time_stamp)
    # Mon Nov 06 15:30:02 2017
    print time.strftime("%Y-%m-%d %H:%M:%S")
    # 2017-11-09 17:17:02
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1509953402))
    # 2017-11-06 15:30:02

    time_stamp = int(time.time())
    print time_stamp
    print divmod(time_stamp, 3600)

if __name__ == '__main__':
    # test_time_consume()
    # test_time()
    # test_sp_mi_sec()
    test_time_transform()
    pass
