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
        # calculate class prior probabilities: P(y=ck)
        self._cal_y_prob(y)

        # calculate Conditional Probability: P( xj | y=ck )
        self._cal_x_prob(x, y)

    def _cal_y_prob(self, y):
        """
        calculate class prior probability
        like: {class_1: prob_1, class_2:prob_2, ...}
        for example two class 1, 2 with probability 0.4 and 0.6
        {1: 0.4, 2: 0.6}
        """
        sample_num = len(y) * 1.0
        if sample_num < 1:
            raise ValueError

        unique_class, class_count = np.unique(y, return_counts=True)

        # calculate class prior probability
        for c, num in zip(unique_class, class_count):
            # use round just for more readable
            # 0.4444444444444444 -> 0.44
            prob = round(num / sample_num, 2)
            self._dic_class_prior[c] = prob

    def _cal_x_prob(self, x, y):
        """
        calculate Conditional Probability: P( xj | y=ck )
        like { c0:{ x0:{ value0:0.2, value1:0.8 }, x1:{} }, c1:{...} }

        for example the below ,as to class 1 feature 0 has 3 values "1, 2 , 3"
        the corresponding probability 0.22, 0.33, 0.44
        p( x1 = 1 | y = 1 ) = 0.22
        p( x1 = 2 | y = 1 ) = 0.33
        p( x1 = 3 | y = 1 ) = 0.44

        { 1: {0: {1: 0.22, 2: 0.33, 3: 0.44}, 1: {4: 0.11, 5: 0.44, 6: 0.44}},
         -1: {0: {1: 0.50, 2: 0.33, 3: 0.16}, 1: {4: 0.50, 5: 0.33, 6: 0.16}}
        }
        """

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
                    prob = round(dic_f_prob[k] * 1.0 / len(c_idxs), 2)
                    dic_f_prob[k] = prob

    def _pred_once(self, x):
        dic_ret = {}

        for y in self._dic_class_prior:
            y_prob = self._dic_class_prior[y]
            for i, v in enumerate(x):
                y_prob = y_prob * self._cd_prob[y][i][v]

            dic_ret[y] = round(y_prob, 2)

        return dic_ret

    def predict(self, x):
        if x.ndim == 1:
            return self._pred_once(x)
        else:
            labels = []
            for i in xrange(x.shape[0]):
                labels.append(self._pred_once(x[i]))

        return labels

    def get_class_prior(self):
        return self._dic_class_prior

    def get_cd_prob(self):
        return self._cd_prob


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
    print x.ndim, y.ndim
    # 2 1

    mnb = MultinomialNB()
    mnb.fit(x, y)

    print "class prior probability: %s" % mnb.get_class_prior()
    # {1: 0.599, -1: 0.40}

    print "feature condition probability: %s" % mnb.get_cd_prob()
    # { 1: {0: {1: 0.22, 2: 0.33, 3: 0.44}, 1: {4: 0.11, 5: 0.44, 6: 0.44}},
    #  -1: {0: {1: 0.50, 2: 0.33, 3: 0.16}, 1: {4: 0.50, 5: 0.33, 6: 0.16}}
    # }

    item = np.array([2, 4])
    print mnb.predict(item)
    # {1: 0.02222, -1: 0.06666}

    pass
