# coding:utf-8

import numpy as np


class DTree(object):
    def __init__(self):
        pass

    def _cal_entropy(self, arr_prob):
        """
        for example  arr_prob like [0.5, 0.5]
        return -1 * 0.5 *log0.5 + -1 * 0.5 * log0.5 = 1
        :param arr_prob: one dimension probability array
        :return: entropy
        """
        # -1 * sum(Pi * logPi)
        return np.sum(-1 * np.log2(arr_prob) * arr_prob)


def get_data():
    x = [[0, 0, 0, 0, 'N'],
               [0, 0, 0, 1, 'N'],
               [1, 0, 0, 0, 'Y'],
               [2, 1, 0, 0, 'Y'],
               [2, 2, 1, 0, 'Y'],
               [2, 2, 1, 1, 'N'],
               [1, 2, 1, 1, 'Y']]

    y = ['outlook', 'temperature', 'humidity', 'windy']
    return x, y

if __name__ == '__main__':

    dt = DTree()

    pass
