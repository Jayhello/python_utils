# _*_ coding:utf-8 _*_

import numpy as np
from sklearn.metrics import accuracy_score


def accuracy_score_demo():
    y_pred = [0, 2, 1, 3]
    y_true = [0, 1, 2, 3]
    print accuracy_score(y_true, y_pred)
    # 0.5

if __name__ == '__main__':
    accuracy_score_demo()
    pass
