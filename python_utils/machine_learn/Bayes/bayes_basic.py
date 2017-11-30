# _*_ coding:utf-8 _*_

"""

"""

import numpy as np


class MultinomialNB(object):
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.classes = None

    def fit(self, x, y):
        pass

    def predict(self, x):
        pass


def get_multi_data():
    x = np.array([
        [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
        [4, 5, 5, 4, 4, 4, 5, 5, 6, 6, 6, 5, 5, 6, 6]
    ])

    x = x.T

    y = np.array([-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1])
    return x, y

if __name__ == '__main__':

    p = {1: {1: 0.1, 2: 0.3}, 2: {1: 0.1, 2: 0.3}}
    print p
    # {1: {1: 0.1, 2: 0.3}, 2: {1: 0.1, 2: 0.3}}
    print p[2], p[2][2]
    # {1: 0.1, 2: 0.3} 0.3

    pass
