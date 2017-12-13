# _*_ coding:utf-8 _*_

import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report


def accuracy_score_demo():
    y_true = [0, 1, 2, 3, 2, 6]
    y_pred = [0, 2, 1, 3, 4, 7]
    print accuracy_score(y_true, y_pred)
    # 0.5
    print confusion_matrix(y_true, y_pred)

    y_true = [0, 1, 0, 1, 1, 0, 1, 0, 1]
    y_pred = [0, 0, 1, 0, 0, 0, 1, 1, 0]
    print confusion_matrix(y_true, y_pred)
    # [[2 2]    四个 0 两个被识别为了 0， 两个被识别为 1
    #  [4 1]]   五个 1 四个被识别为了 0， 一个被识别为 1


def classification_report_demo():
    y_pred = [0, 0, 2, 1, 0]
    y_true = [0, 1, 2, 2, 0]
    target_names = ['class 0', 'class 1', 'class 2']
    print classification_report(y_true, y_pred, target_names=target_names)

    print confusion_matrix(y_true, y_pred)
    # [[2 0 0]
    #  [1 0 0]
    #  [0 1 1]]

if __name__ == '__main__':
    classification_report_demo()
    # accuracy_score_demo()
    pass
