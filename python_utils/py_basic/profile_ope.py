# coding:utf-8

import cProfile


def func1():
    sum = 0
    for i in range(1000000):
        sum += i

    #  1    0.167    0.167    0.167    0.167 {range}
    #  4 function calls in 0.674 seconds


def func2():
    sum = 0
    for i in xrange(1000000):
        sum += i

    # 3 function calls in 0.350 seconds

if __name__ == '__main__':
    # cProfile.run("func1()")
    cProfile.run("func2()")
    pass
