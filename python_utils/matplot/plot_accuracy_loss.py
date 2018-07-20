# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt


def draw_result(lst_iter, lst_loss, lst_acc, title):
    plt.plot(lst_iter, lst_loss, '-b', label='loss')
    plt.plot(lst_iter, lst_acc, '-r', label='accuracy')

    plt.xlabel("n iteration")
    plt.legend(loc='upper left')
    plt.title(title)
    plt.savefig(title+".png")  # should before show method

    plt.show()


def test_draw():
    lst_iter = range(100)
    lst_loss = [0.01 * i - 0.01 * i ** 2 for i in xrange(100)]
    # lst_loss = np.random.randn(1, 100).reshape((100, ))
    lst_acc = [0.01 * i + 0.01 * i ** 2 for i in xrange(100)]
    # lst_acc = np.random.randn(1, 100).reshape((100, ))
    draw_result(lst_iter, lst_loss, lst_acc, "sgd_method")


if __name__ == '__main__':
    test_draw()
    pass
