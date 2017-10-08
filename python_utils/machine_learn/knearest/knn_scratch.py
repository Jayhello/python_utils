# _*_ coding:utf-8 _*_
"""
implement knn from scratch
"""
from collections import Counter
import numpy as np


class KnnScratch(object):

    def predict_once(self, x_train, y_train, x_test, k):
        lst_distance = []
        lst_predict = []

        for i in xrange(len(x_train)):
            distance = np.sqrt(np.sum(np.square(x_test, x_train[i, :])))
            lst_distance.append(distance)

        lst_distance = sorted(lst_distance)

        for i in xrange(k):
            idx = lst_distance[i][1]
            lst_predict.append(y_train[idx])

        return Counter(lst_predict).most_common(1)[0][0]

    def predict(self, x_train, y_train, x_test, k):
        lst_predict = []


if __name__ == '__main__':

    pass