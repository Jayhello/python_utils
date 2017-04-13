# _*_ coding:utf-8 _*_
"""
This file is about thread(dummy)/process pool
"""
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
import logging
from time import sleep, time
from random import randrange


# logging.basicConfig(level=logging.DEBUG,
#                     format='%(levelname)s %(asctime)s %(threadName)s %(message)s',
#                     datefmt='%Y-%m-%d %I:%M:%S')

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s %(asctime)s %(processName)s %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S')


def handler(sec):
    logging.debug('now I will sleep %s S', sec)
    sleep(sec)


def get_pool(b_dummy=True, num=4):
    """
    if b_dummy is True then get ThreadPool, or get process pool
    :param b_dummy: dummy thread Pool or Process pool
    :param num: thread or process num
    :return: pool object
    """
    if b_dummy:
        pool = ThreadPool(num)
    else:
        pool = ProcessPool(num)

    return pool


def test_dummy_thread_pool():
    start_time = time()
    lst_sleep_sec = [randrange(3, 10) for i in xrange(10)]
    pool = get_pool(b_dummy=False)

    results = pool.map(handler, lst_sleep_sec)
    logging.debug(results)
    pool.close()
    pool.join()
    logging.debug('time consume %s', time() - start_time)
    pass


if __name__ == '__main__':
    test_dummy_thread_pool()
    pass
