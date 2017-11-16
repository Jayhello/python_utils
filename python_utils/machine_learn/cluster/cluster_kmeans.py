# _*_ coding:utf-8 _*_

import numpy as np
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt


def get_k_data():
    x, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)
    # plt.scatter(x[:, 0], x[:, 1])
    # plt.show()
    print y
    return x


def init_board_gauss(N, k):
    from numpy import random
    n = float(N)/k
    X = []
    for i in range(k):
        c = (random.uniform(-1, 1), random.uniform(-1, 1))
        s = random.uniform(0.05, 0.5)
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
    def __init__(self, k, init_vec, max_iter=100):
        """
        :param k:
        :param init_vec: init mean vectors
        """
        self._k = k
        self._cluster_vec = init_vec
        self._max_iter = max_iter

    def fit(self, x):
        pass

    def _cal_distance(self, vec1, vec2):
        return np.linalg.norm(vec1 - vec2)

    def _cluster(self, x):
        # 每个簇心对应的簇节点
        lst_cluster_idx = []

        for x_node in x:
            lst_dis = []
            for c_node in self._cluster_vec:
                d = self._cal_distance(c_node, x_node)
                lst_dis.append(d)


    def _check_converge(self):
        pass

if __name__ == '__main__':
    # x = init_board_gauss(200, 3)
    x = get_k_data()
    # plt.scatter(x[:, 0], x[:, 1], c='r')
    # plt.show()
    pass
