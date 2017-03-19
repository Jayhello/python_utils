# _*_ coding:utf-8 _*_
import numpy as np
import sys
from utils.FileUtil import get_line_lst


date_path = '../dataset/perception/dataset.txt'
train_set = []


class Perception(object):

    def __init__(self, var_num):
        self.w = np.random.randn(var_num, 1)
        self.b = 1
        self.var_num = var_num
        self.min_error_rate = 0.02

    def train(self, train_data, eta):
        """
        training model
        :param train_data: array like [[1, 2, 0], [1.1, 0.8, 1]]
        :param eta: learning rate:
        :return none:
        """
        for item in train_data:
            output = self.w * item[0:-1] + self.b
            output = 1 if output >= 0 else -1
            error = True if output != item[-1] else False

            if error:
                self.w += output * item[0:-1]
                self.b += output

    def sdg(self, train_data, epoch, eta):

        for i in xrange(epoch):
            self.train(train_data, eta)

            current_error_rate = self.get_error_rate(train_data)
            print 'epoch {0} current_error_rate: {1}'.format(i+1, current_error_rate)
            if current_error_rate <= self.min_error_rate:
                break

    def get_error_rate(self, validate_data):
        return 0

    def get_current_para(self):
        return self.w, self.b

def generate_date():
    lst_data = get_line_lst(date_path)

    lst_ret = []
    for item in lst_data:
        lst_ret.append(item.split())

    return np.array(lst_ret)

if __name__ == '__main__':
    print generate_date()[0]
    print generate_date()[0][0:-1]
    # var_num = 2
    # p = Perception(var_num)
    # print p.get_current_para()[0]
