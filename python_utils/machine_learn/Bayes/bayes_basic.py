# _*_ coding:utf-8 _*_

"""

"""

import numpy as np


class MultinomialNB(object):
    def __init__(self, alpha=1.0):
        self.alpha = alpha

        self._dic_class_prior = {}
        self._cd_prob = {}

    def fit(self, x, y):
        self._cal_y_prob(y)
        self._cal_x_prob(x, y)

    def _cal_y_prob(self, y):
        """calculate label probability"""
        sample_num = len(y) * 1.0
        if sample_num < 1:
            raise ValueError

        unique_class, class_count = np.unique(y, return_counts=True)

        # calculate class prior probability
        for c, num in zip(unique_class, class_count):
            self._dic_class_prior[c] = num / sample_num

    def _cal_x_prob(self, x, y):
        """calculate input feature probability"""

        unique_class = np.unique(y)

        for c in unique_class:
            self._cd_prob[c] = {}

            c_idxs = np.where(y==c)[0]

            for i, col_feature in enumerate(x.T):
                dic_f_prob = {}
                self._cd_prob[c][i] = dic_f_prob

                for idx in c_idxs:
                    if col_feature[idx] in dic_f_prob:
                        dic_f_prob[col_feature[idx]] += 1
                    else:
                        dic_f_prob[col_feature[idx]] = 1

                for k in dic_f_prob:
                    dic_f_prob[k] = dic_f_prob[k] * 1.0 / len(c_idxs)

    def _pred_once(self, x):
        dic_ret = {}

        for y in self._dic_class_prior:
            y_prob = self._dic_class_prior[y]
            for i, v in enumerate(x):
                y_prob = y_prob * self._cd_prob[y][i][v]

            dic_ret[y] = y_prob

        return dic_ret

    def predict(self, x):
        pass


def get_multi_data():
    x = np.array([
        [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
        [4, 5, 5, 4, 4, 4, 5, 5, 6, 6, 6, 5, 5, 6, 6]
    ])

    x = x.T

    y = np.array([-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1])
    return x, y

if __name__ == '__main__':

    x, y = get_multi_data()
    mnb = MultinomialNB()
    mnb.fit(x, y)

    item = np.array([2, 4])
    print mnb._pred_once(item)

    print x.ndim, y.ndim

    p = {1: {1: 0.1, 2: 0.3}, 2: {1: 0.1, 2: 0.3}}
    print p
    # {1: {1: 0.1, 2: 0.3}, 2: {1: 0.1, 2: 0.3}}
    print p[2], p[2][2]
    # {1: 0.1, 2: 0.3} 0.3

    pass
