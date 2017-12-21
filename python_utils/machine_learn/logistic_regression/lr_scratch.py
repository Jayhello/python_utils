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
        return 1.0 / (1 + np.exp(x))

    def fit(self, X, Y, **opt):
        m, n = X.shape
        self._weight = np.ones((n, 1))
        max_iter = opt.get("max_iter", 100)
        alpha = opt.get("alpha", 0.01)
        method = opt.get("method", "sgd")

        for k in xrange(max_iter):
            try:
                self._do_train[method](X, Y, alpha)
            except KeyError:
                raise ValueError('method error')

    def _sgd(self):
        """stochastic gradient descent"""
        pass

    def _gd(self, X, Y, alpha):
        """gradient descent"""
        pred = self._sigmoid(X * self._weight)
        error = Y - pred
        self._weight = self._weight + alpha * X.transpose() * error


def get_data():
    path = '../dataset/logistic_regression/lr_ml_action.txt'
    # dataset = pd.read_csv(path, sep='\t', header=None, names=['f1', 'f2', 'label'])
    # dataset = pd.read_csv(path, header=None)
    dataset = pd.read_csv(path, delim_whitespace=True,
                          names=['f1', 'f2', 'label'],
                          dtype={'A': np.float64, 'B': np.float64, 'C': np.int64})
    # dataset.columns = ['f1', 'f2', 'label']
    print dataset.head()

if __name__ == '__main__':
    get_data()
    pass
