# _*_ coding:utf-8 _*_
"""
This file is about a sample demo about threading.condition
"""

import threading
import time
import logging
from basic_thread import join_all_others_thread
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(threadName)s %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S')


def notify_condition(con):
    with con:
        logging.debug('now notify all the condition')
        con.notifyAll()


def wait_condition(con):
    with con:
        logging.debug('I am waiting for an condition')
        con.wait()
        logging.debug('I get the condition.....')


def test_demo():
    con = threading.Condition()
    t_w1 = threading.Thread(name='t_w1', target=wait_condition, args=(con, ))
    t_w2 = threading.Thread(name='t_w2', target=wait_condition, args=(con, ))
    t_n1 = threading.Thread(name='t_n1', target=notify_condition, args=(con, ))
    t_w1.start()
    t_w2.start()

    logging.debug('now main thread sleeping 5S')
    time.sleep(5)
    t_n1.start()

    join_all_others_thread()
    logging.debug('now all have been done')

if __name__ == '__main__':
    test_demo()
    pass
