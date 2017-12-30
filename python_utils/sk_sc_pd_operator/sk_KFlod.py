# coding:utf-8
"""
http://scikit-learn.org/stable/modules/cross_validation.html
"""


import pandas as pd
import numpy as np
from sklearn.model_selection import KFold


def kfold_1():
    X = np.array([[3, 4, 0], [3, 2, 1], [5, 6, 0],
                  [1, 2, 1], [1, 5, 0], [7, 4, 1]])
    kf = KFold(n_splits=4)
    for train, test in kf.split(X):
        print "=======train: %s" % X[train].tolist()
        # print X[train]
        print "=======test : %s" % X[test].tolist()


if __name__ == '__main__':
    kfold_1()
    pass
