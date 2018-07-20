# coding:utf-8

import numpy as np


def log2_test():
    arr = np.array([0, 1, 2, 3, 2 ** 4])
    print np.log2(arr)
    # [-inf, 0, 1, 1.5849625, 4]

    arr = np.array([1, 2, 4, 2 ** 3])
    arr_lg = np.log2(arr)
    print arr_lg
    # [ 0.  1.  2.  3.]
    print arr_lg * arr
    # [  0.   2.   8.  24.]

    # calculate entropy
    print np.sum(arr_lg * arr)
    # 34


def cal_entropy():
    arr1 = np.array([0.5, 0.5])
    print np.log2(arr1)
    # [-1. -1.]

    print np.sum(np.log2(arr1) * arr1)
    # -1.0

    print np.sum(-1 * np.log2(arr1) * arr1)
    # 1.0

    arr2 = np.array([0.1, 0.9])
    print np.sum(-1 * np.log2(arr2) * arr2)
    # 0.468995593589


class SoftmaxLayer:
    def __init__(self, name='Softmax'):
        pass

    def forward(self, in_data):
        shift_scores = in_data - np.max(in_data, axis=1).reshape(-1, 1)
        self.top_val = np.exp(shift_scores) / np.sum(np.exp(shift_scores), axis=1).reshape(-1, 1)
        return self.top_val

    def backward(self, residual):
        N = residual.shape[0]
        dscores = self.top_val.copy()
        dscores[range(N), list(residual)] -= 1
        dscores /= N
        return dscores


def test_log():
    arr1 = np.array([[-0.1, -0.2, -0.3], [0.1, 0.2, 0.4]])
    sl = SoftmaxLayer()
    # print sl.forward(arr1)

    # print np.max(arr1, axis=1).reshape(-1, 1)

    arr2 = np.array([[1, 2, 3], [-1, -2, -4]])
    # print sl.forward(arr2)

    arr_base = np.array([2, 2, np.e])
    arr_log = np.array([1, 2, 4])
    print np.log([arr_base, arr_log])


if __name__ == '__main__':
    test_log()
    # log2_test()
    # cal_entropy()
    pass
