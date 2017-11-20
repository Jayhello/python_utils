# _*_ coding:utf-8 _*_

"""
cited from
"""

import numpy as np
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
import operator


def get_k_data():
    x, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)
    # plt.scatter(x[:, 0], x[:, 1])
    # plt.show()
    # print y
    return x, y


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
        :param init_vec: init mean vectors type: k * n array(n properties)
        """
        self._k = k
        self._cluster_vec = init_vec
        self._max_iter = max_iter

    def fit(self, x):
        for i in xrange(self._max_iter):
            print 'iteration %s' % i
            d_cluster = self._cluster_point(x)
            new_center_node = self._reevaluate_center_node(d_cluster)

            if self._check_converge(new_center_node):
                print 'found converge node'
                break
            else:
                self._cluster_vec = new_center_node

    def _cal_distance(self, vec1, vec2):
        return np.linalg.norm(vec1 - vec2)

    def _cluster_point(self, x):
        # 每个簇心对应的簇节点
        lst_cluster_idx = []
        d_cluster = {}

        for x_node in x:
            lst_dis = []
            for c_node in self._cluster_vec:
                d = self._cal_distance(c_node, x_node)
                lst_dis.append(d)
            min_idx, min_dis = min(enumerate(lst_dis), key=operator.itemgetter(1))
            lst_cluster_idx.append(min_idx)

        for i, idx in enumerate(lst_cluster_idx):
            if idx not in d_cluster.keys():
                d_cluster[idx] = np.array([x[i]])
            else:
                d_cluster[idx] = np.append(d_cluster[idx], [x[i]], axis=0)

        return d_cluster

    def _reevaluate_center_node(self, d_cluster):
        arr_center_node = np.empty_like(self._cluster_vec)
        for i, k in enumerate(d_cluster.keys()):
            arr_center_node[i] = np.mean(d_cluster[k], axis=0)

        return arr_center_node

    def _check_converge(self, vec):
        return np.array_equal(self._cluster_vec, vec)

    def get_center_node(self):
        return self._cluster_vec

    def pred(self, arr_data):
        """
        :param arr_data: numpy array
        :return:
        """
        ret_lst_label =[]
        for sample in arr_data:
            lst_d = []
            for node in self._cluster_vec:
                d = self._cal_distance(sample, node)
                lst_d.append(d)

            label, min_d = min(enumerate(lst_d), key=operator.itemgetter(1))
            ret_lst_label.append(label)

        return ret_lst_label


def plot_cluster(x, center_node):
    plt.scatter(x[:, 0], x[:, 1], s=20)
    plt.scatter(center_node[:, 0], center_node[:, 1], c='black', s=200, alpha=0.5)
    plt.show()

if __name__ == '__main__':
    # x data set, y labels
    x, y = get_k_data()
    # plt.scatter(x[:, 0], x[:, 1], c='r')
    # plt.show()
    k = 4
    lst_idx = np.random.randint(x.shape[0], size=k)
    print lst_idx
    # [163 283 157 282]
    init_vec = x[lst_idx]
    print init_vec

    # plot_cluster(x, init_vec)
    # [[-0.73069817  6.24208856]
    #  [ 1.87271752  4.18069237]
    # [-1.81487687  7.9783219 ]
    # [-1.4136581   7.40962324]]

    print y[lst_idx]
    # [1 3 2 2]
    km = KMeans(k, init_vec)
    km.fit(x)

    plot_cluster(x, km.get_center_node())

    print km.pred(init_vec)
    # [0, 1, 2, 2]
    pass
