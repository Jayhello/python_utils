# coding=utf-8
"""
计算型的任务，使用多线程GIL就会让多线程变慢。我们举个计算斐波那契数列的例子
http://www.dongwm.com/archives/%E4%BD%BF%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-%E7%BA%BF%E7%A8%8B%E7%AF%87/

"""

import time
import threading


def profile(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print 'COST: {}'.format(end - start)
    return wrapper


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


@profile
def nothread():
    fib(35)
    fib(35)


@profile
def hasthread():
    for i in range(2):
        t = threading.Thread(target=fib, args=(35,))
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()

if __name__ == '__main__':
    nothread()
    # COST: 16.8039999008
    hasthread()
    # COST: 42.8039999008
