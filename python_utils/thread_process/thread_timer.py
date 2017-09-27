# _*_ coding:utf-8 _*_
"""
python timer usage cited from:
http://www.bogotobogo.com/python/Multithread/python_multithreading_subclassing_Timer_Object.php
https://stackoverflow.com/questions/16578652/threading-timer

repeat timer
https://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds
"""

import time
import threading


def hello():
    print 'hello world'


def hello_2(name):
    print 'hello %s \n' % name


def test_timer_no_para():
    """no parameter timer test
    """
    t = threading.Timer(5, hello)
    # the method will be executed after 5 S
    # just run once, then exit
    t.start()


def test_timer_with_para():
    """no parameter timer test
    """
    name = 'bear fish'
    t = threading.Timer(5, hello_2, [name])
    # the method will be executed after 5 S
    # just run once, then exit
    t.start()

if __name__ == '__main__':
    test_timer_no_para()
    test_timer_with_para()
    pass
