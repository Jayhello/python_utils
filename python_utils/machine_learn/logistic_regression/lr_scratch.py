# coding:utf-8

import numpy as np
import pandas as pd


class LogisticRegression(object):
    def __init__(self):
        self._map_method()
        pass

    def _map_method(self):
        self._do_train = {"gd": self._gd, "sgd": self._sgd}

    def _sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))

    def fit(self, X, Y, **opt):
        m, n = X.shape
        self._weight = np.ones((n, 1))
        max_iter = opt.get("max_iter", 100)
        alpha = opt.get("alpha", 0.01)
        method = opt.get("method", "sgd")

        for k in xrange(max_iter):
            try:
                self._do_train[method](X, Y, alpha)

                print "iter %s error rate %s" % (k, self._get_error_rate(X, Y))
            except KeyError:
                raise ValueError('method error')

    def _sgd(self, X, Y, alpha):
        """stochastic gradient descent"""
        m, n = X.shape
        for i in xrange(m):
            # pred = self._sigmoid(X[i, :] * self._weight)
            pred = self._sigmoid(np.dot(X[i, :], self._weight))
            error = Y[i] - pred
            self._weight = self._weight + alpha * np.matrix(X[i, :]).T * error

    def _gd(self, X, Y, alpha):
        """gradient descent"""
        pred = self._sigmoid(X * self._weight)
        error = Y - pred
        self._weight = self._weight + alpha * X.T * error

    def _get_error_rate(self, X, Y):
        all_num = len(Y)
        error_num = 0
        for i in xrange(all_num):
            pred = self._sigmoid(np.dot(X[i, :], self._weight)) > 0.5
            if pred != bool(Y[i]):
                error_num += 1

        return error_num * 1.0 / all_num


def get_data():
    path = '../dataset/logistic_regression/lr_ml_action.txt'

    data = pd.read_csv(path, delim_whitespace=True,
                          names=['f1', 'f2', 'label'],
                          dtype={'A': np.float64, 'B': np.float64, 'C': np.int64})

    # add bias w0
    data['f0'] = 1
    print data.head()
    features = ['f0', 'f1', 'f2']
    return data[features].values, data.label.values


def test_lr():
    X, Y = get_data()

    lr = LogisticRegression()
    arr = np.array([-1, 0, 1])
    print lr._sigmoid(arr)
    lr.fit(X, Y)


if __name__ == '__main__':
    # get_data()
    test_lr()
    pass
