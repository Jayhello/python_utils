# _*_ coding:utf-8 _*_

"""
This file is about operator of threading.Lock
using which we can realize a thread safe counter
"""

import logging
import threading
import random
import time


logging.basicConfig(level=logging.DEBUG,
                    format='(%(asctime)s %(threadName)-10s) %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S')


class CounterThreadSafe(threading.Thread):
    def __init__(self, start=0):
        super(CounterThreadSafe, self).__init__()
        self.val = start
        self.lock = threading.Lock()

    def inc(self, num):
        try:
            logging.debug('wanting for lock, before num is %s val is %s', num, self.val)
            self.lock.acquire()
            self.val += num
            logging.debug('after counter val is %s', self.val)
        finally:
            self.lock.release()

    def inc_v2(self, num):
        logging.debug('wanting for lock, before num is %s val is %s', num, self.val)
        with self.lock:
            self.val += num
        logging.debug('after counter val is %s', self.val)

g_sum = 0


def do_counter(counter):
    global g_sum
    for i in xrange(0, 2):
        sleep_sec = random.randint(1, 3)
        logging.debug('now sleeping %s S', sleep_sec)
        g_sum += sleep_sec
        time.sleep(sleep_sec)
        # counter.inc(sleep_sec)
        counter.inc_v2(sleep_sec)


def test_multi_thread_counter():
    counter = CounterThreadSafe()

    for i in xrange(0, 5):
        t = threading.Thread(target=do_counter, args=(counter, ))
        t.start()
        # t.join()   # can't join in this row or it will block the main thread

    logging.debug('start all thread.....done')


def join_all_others_thread():
    logging.debug('now join all the other threads')
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()

    # the following msg will be print after all the other thread done
    logging.debug('join all the other threads success')


if __name__ == '__main__':
    test_multi_thread_counter()
    join_all_others_thread()
    # the following msg will be print after all the other thread done
    logging.debug('all the sub threads done')
    logging.debug('g_sum is %s', g_sum)
    pass
