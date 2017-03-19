# _*_ coding:utf-8 _*_
import numpy as np
import sys
from utils.FileUtil import get_line_lst


date_path = '../dataset/perception/dataset.txt'
train_set = []


class Perception(object):

    def __init__(self, var_num):
        self.w = np.random.randn(1, var_num)
        self.b = 1
        self.var_num = var_num
        self.min_error_rate = 0.02

    def get_current_para(self):
        return self.w, self.b

    def train(self, train_data, eta):
        pass

    def SGD(self, train_data, epoch, eta):

        for i in xrange(epoch):
            self.train(train_data, eta)

            current_error_rate = self.get_error_rate(train_data)
            print 'epoch {0} current_error_rate: {1}'.format(i+1, current_error_rate)
            if current_error_rate <= self.min_error_rate:
                break

    def get_error_rate(self, validate_data):
        return 0


def generate_date():
    lst_data = get_line_lst(date_path)

    lst_ret = []
    for item in lst_data:
        lst_ret.append(item.split())

    return lst_ret

if __name__ == '__main__':
    # generate_date()
    var_num = 2
    # p = Perception(var_num)
    # print p.get_current_para()[0]

    # arr1 = np.array([1, 2])
    # arr2 = np.array([3, 4])
    # print arr1 * arr2
    # print np.dot(arr1, arr2.transpose())
    tp = (1, 2, 3)
    lst = [[1, 2], [3, 4, 5]]
    lst = [[1, 2], [3, 4]]
    print np.array(lst).shape
    print np.array(lst)
    print np.asarray(lst)
    print np.asarray(tp)