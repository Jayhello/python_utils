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
            logging.debug('wanting for lock')
            self.lock.acquire()
            self.val += num
            logging.debug('now counter add %s', num)
        finally:
            self.lock.release()


def do_counter(counter):
    for i in xrange(0, 2):
        sleep_sec = random.randint(6, 10)
        logging.debug('now sleeping %s S', sleep_sec)
        time.sleep(sleep_sec)
        counter.inc(sleep_sec)


def test_multi_thread_counter():
    counter = CounterThreadSafe()

    for i in xrange(0, 3):
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
    pass
