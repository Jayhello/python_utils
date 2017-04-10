# _*_ coding:utf-8 _*_
"""
This file is about subplot
mainly cited from `http://matplotlib.org/examples/pylab_examples/subplots_demo.html`
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_mul():
    left, width = 0.1, 0.8
    ax1 = plt.axes([left, 0.5, width, 0.45])
    ax2 = plt.axes([left, 0.3, width, 0.19])
    ax3 = plt.axes([left, 0.2, width, 0.09], sharex=ax2)
    ax4 = plt.axes([left, 0.1, width, 0.09], sharex=ax2)

    # ticks at the top of the top plot
    ax1.xaxis.tick_top()
    # remove ticks for ax2 and ax3
    ax2.xaxis.set_visible(False)
    ax3.xaxis.set_visible(False)

    # only put ticks on the bottom of ax4
    ax4.xaxis.tick_bottom()
    plt.show()


def subplot_demo1():
    # Simple data to display in various forms
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    # Just a figure and one subplot
    f, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Simple plot')
    plt.show()


def subplot_demo2():
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    f, ax_arr = plt.subplots(2, sharex=True)
    ax_arr[0].plot(x, y)
    ax_arr[0].set_title('sharing x axis')
    ax_arr[1].scatter(x, y)
    plt.show()


def subplot_demo3():
    # Two subplots, unpack the axes array immediately
    x = np.linspace(0, 2 * np.pi, 300)
    y = np.sin(x ** 2)

    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.plot(x, y)
    ax1.set_title('Sharing Y axis')
    ax2.scatter(x, y)

    plt.show()


def subplots_demo4():
    x = np.linspace(0, 2 * np.pi, 300)
    y = np.sin(x ** 2)

    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
    ax1.plot(x, y)
    ax1.set_title('sharing x axis')

    ax2.scatter(x, y)

    x1 = [1, 2, 3, 4, 5, 6, 7]
    y1 = [2.6, 3.6, 8.3, 56, 12.7, 8.9, 5.3]
    ax3.scatter(x1, y1)
    plt.show()

if __name__ == '__main__':
    # plot_mul()
    # subplot_demo1()
    # subplot_demo2()
    # subplot_demo3()
    subplots_demo4()
    pass
