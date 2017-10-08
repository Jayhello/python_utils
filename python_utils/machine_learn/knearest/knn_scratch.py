# _*_ coding:utf-8 _*_
"""
implement knn from scratch
"""
from collections import Counter
import numpy as np


class KnnScratch(object):

    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict_once(self, x_test, k):
        lst_distance = []
        lst_predict = []

        for i in xrange(len(self.x_train)):
            # euclidean distance
            distance = np.linalg.norm(x_test - self.x_train[i, :])
            # distance = np.sqrt(np.sum(np.square(x_test, x_train[i, :])))
            lst_distance.append([distance, i])

        lst_distance = sorted(lst_distance)

        for i in xrange(k):
            idx = lst_distance[i][1]
            lst_predict.append(self.y_train[idx])

        return Counter(lst_predict).most_common(1)[0][0]

    def predict(self, x_test, k):
        lst_predict = []
        for i in xrange(len(x_test)):
            lst_predict.append(self.predict_once(x_test[i, :], k))

        return lst_predict

if __name__ == '__main__':
    x_train = np.array([[1, 1, 1], [2, 2, 2], [10, 10, 10], [13, 13, 13]])
    y_train = ['aa', 'aa', 'bb', 'bb']
    x_test = np.array([[3, 2, 4], [9, 13, 11]])

    knn = KnnScratch()
    knn.fit(x_train, y_train)
    print knn.predict(x_test, 2)
    # ['aa', 'bb']
    pass
