# _*_ coding:utf-8 _*_

import time
import threading


def hello():
    print 'hello world'


def test_timer_no_para():
    """no parameter timer test"""
    t = threading.Timer(5, hello)
    t.start()

if __name__ == '__main__':
    test_timer_no_para()
    pass
