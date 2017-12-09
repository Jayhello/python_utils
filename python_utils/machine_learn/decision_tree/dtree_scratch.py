# coding:utf-8

import numpy as np


class DTree(object):
    def __init__(self):
        pass

    def _cal_entropy(self, arr_prob):
        """
        for example  arr_prob like [0.5, 0.5]
        return -1 * 0.5 *log0.5 + -1 * 0.5 * log0.5 = 1
        :param arr_prob: one dimension probability array
        :return: entropy
        """
        # -1 * sum(Pi * logPi)
        return np.sum(-1 * np.log2(arr_prob) * arr_prob)

    def _cal_conditional_entropy(self, X, Y):
        """
        calculate conditional entropy H(D|A)
        :return:
        """
        pass

    def _cal_class_entropy(self, y):
        """
        calculate data set entropy

        :param y:
        :return:
        """
        num = len(y)
        print num  # 15
        unique_class, counter = np.unique(y, return_counts=True)
        print unique_class, counter
        # [0 1] [6 9]
        # calculate each class probability
        class_prob = [c * 1.0 / num for c in counter]
        print class_prob
        # [0.40000000000000002, 0.59999999999999998]
        print self._cal_entropy(class_prob)
        # 0.970950594455


def test_cal_class_entropy():
    from create_data import get_loan_data_lh
    X, Y = get_loan_data_lh()
    dt = DTree()
    dt._cal_class_entropy(Y)

if __name__ == '__main__':
    test_cal_class_entropy()
    # dt = DTree()

    pass
