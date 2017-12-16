# coding:utf-8

import numpy as np
import pandas as pd


class LogisticRegression(object):
    def __init__(self):
        pass

    def sigmoid(self, x):
        return 1.0 / (1 + np.exp(x))

    def fit(self, x, y, alpha):
        pass


def get_data():
    path = '../dataset/logistic_regression/lr_ml_action.txt'
    # dataset = pd.read_csv(path, sep='\t', header=None, names=['f1', 'f2', 'label'])
    dataset = pd.read_csv(path, header=None)
    # dataset.columns = ['f1', 'f2', 'label']
    print dataset.head()

if __name__ == '__main__':
    get_data()
    pass
