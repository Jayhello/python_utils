# _*_ coding:utf-8 _*_

import numpy as np
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt


def get_k_data():
    x, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)
    # plt.scatter(x[:, 0], x[:, 1])
    # plt.show()
    return x


def init_board_gauss(N, k):
    from numpy import random
    n = float(N)/k
    X = []
    for i in range(k):
        c = (random.uniform(-1, 1), random.uniform(-1, 1))
        s = random.uniform(0.05,0.5)
        x = []
        while len(x) < n:
            a, b = np.array([np.random.normal(c[0], s), np.random.normal(c[1], s)])
            # Continue drawing points from the distribution in the range [-1,1]
            if abs(a) < 1 and abs(b) < 1:
                x.append([a, b])
        X.extend(x)
    X = np.array(X)[:N]
    return X


class KMeans(object):
    def __init__(self, data_set, k, init_vec):
        """
        :param data_set:
        :param k:
        :param init_vec: init mean vectors
        """
        self._data_set = data_set
        self._k = k
        self._init_vec = init_vec

    def cluster(self):
        for node in self._data_set:

            pass

    def _cal_distance(self, x, y):
        pass

    def _check_converge(self):
        pass

if __name__ == '__main__':
    # x = init_board_gauss(200, 3)
    x = get_k_data()
    plt.scatter(x[:, 0], x[:, 1], c='r')
    plt.show()
    pass
