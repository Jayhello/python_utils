# _*_ coding:utf-8 _*_
"""
This file is about `matplotlib`
Mainly cited from http://matplotlib.org/users/pyplot_tutorial.html
"""

import matplotlib.pyplot as plt
import numpy as np
import random


def basic_linear():
    y_lst = [1, 2, 3, 4]
    # y_lst = random.sample(range(80000), 500)
    plt.plot(y_lst)
    plt.ylabel('y axis value')
    plt.show()


def plot_x1_y4():
    """
    plot a line x = 1
    :return:
    """
    plt.plot([0, 0], [0, 4], color='red', linewidth=3.0)
    plt.axis([-1, 1, -4, 4])
    plt.show()


def basic_curve():
    x = np.linspace(0, 2, 11)
    print x
    y = x ** 3 - 5 * x ** 2 + 6 * x + 1
    print y
    # plt.plot(x, y, 'r-')
    # plt.plot(x, y)
    lines = plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.setp(lines, color='r')
    plt.show()
    # plt.axis([0, 100, 0, 100])


def multi_curve():
    t = np.arange(0., 5., 0.2)
    print t
    # plt.plot(t, t, 'r-', t, t**2, 'bs', t, t**3, 'g^')
    # plt.show()


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


def multi_figure():
    plt.figure(1)  # the first figure
    plt.subplot(211)  # the first subplot in the first figure
    plt.plot([1, 2, 3])
    plt.subplot(212)  # the second subplot in the first figure
    plt.plot([4, 5, 6, 7, 11])

    plt.figure(2)  # a second figure
    plt.plot([4, 5, 6])  # creates a subplot(111) by default

    plt.figure(1)  # figure 1 current; subplot(212) still current
    plt.subplot(211)  # make subplot(211) in figure1 current
    plt.title('Easy as 1, 2, 3')  # subplot 211 title

    plt.show()


def multi_figure_two():
    t1 = np.arange(0., 5, 0.1)
    t2 = np.arange(0., 5, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2 * np.pi * t2), 'bo')

    plt.show()


def histogram():
    x_mul = [np.random.randn(n) for n in [1000, 1000, 1000]]
    print x_mul
    bin = 10
    plt.hist(x_mul, bin)
    plt.show()


def histogram_two():
    x_mul = [random.sample(range(0, 100), n) for n in [60, 50, 70]]
    print x_mul[0]
    print x_mul[1]
    print x_mul[2]
    bin = 10
    plt.hist(x_mul, bin)
    plt.show()


def plot_2d():
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [2.6, 3.6, 8.3, 56, 12.7, 8.9, 5.3]
    plt.plot(x, y)      # plot line
    # plt.scatter(x, y)   # plot scatter
    plt.show()


if __name__ == '__main__':
    # plot_2d()
    # basic_linear()
    # basic_curve()
    # multi_curve()
    multi_figure()
    # multi_figure_two()
    # histogram()
    # histogram_two()
    pass
