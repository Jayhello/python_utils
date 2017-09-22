# _*_ coding:utf-8 _*_
import numpy as np
from utils.FileUtil import get_line_lst
import matplotlib.pyplot as plt


class Perception(object):

    def __init__(self, var_num):
        # self.w = np.random.randn(1, var_num)
        self.w = np.ones(var_num)
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
            output = (np.dot(self.w, item[0:-1]) + self.b)*item[-1]
            if output <= 0:
                self.w += eta * item[-1] * item[0:-1]
                self.b += eta * item[-1]

    def sgd(self, train_data, epoch, eta, batch_size):
        """
        Training perception model by stochastic gradient descent
        :param train_data: 2D array like [[1.1, 2.3, -1]] the last
                            item -1 train_date[0][-1] means label
        :param epoch:
        :param eta:learning rate
        :return:none
        """
        for i in xrange(epoch):
            np.random.shuffle(train_data)
            batch_lst = [train_data[k:k+batch_size] for k in xrange(0, len(train_data), batch_size)]
            for mini_batch in batch_lst:
                self.train(mini_batch, eta)

            current_error_rate = self.get_error_rate(train_data)
            print 'epoch {0} current_error_rate: {1}'.format(i+1, current_error_rate)
            print self.get_current_para()
            if current_error_rate <= self.min_error_rate:
                break

    def get_error_rate(self, validate_data):
        all_len = validate_data.shape[0]
        error_len = 0
        for item in validate_data:
            output = np.dot(self.w, item[0:-1]) + self.b
            output = 1 if output >= 0 else -1
            error = True if output != item[-1] else False
            if error:
                error_len += 1

        return float(error_len) / all_len

    def get_current_para(self):
        return self.w, self.b

    def get_weight(self):
        return self.w

    def get_bias(self):
        return self.b


def generate_data(data_path):
    lst_data = get_line_lst(data_path)

    # lst_ret = []
    # for item in lst_data:
    #     lst_ret.append([float(s) for s in item.split()])
    # the following one line  is equivalent to the above for loop
    lst_ret = [[float(s) for s in item.split()] for item in lst_data]

    ret_arr = np.array(lst_ret)

    # change all the label whose value is 0 to -1
    for i in xrange(ret_arr.shape[0]):
        if ret_arr[i][-1] == 0:
            ret_arr[i][-1] = -1

    return ret_arr


def plot_data_scatter(train_data, w, b):
    x = np.linspace(-5, 5, 10)
    plt.figure()
    # 画散点图(plot scatter)
    for i in range(len(train_data)):
        if train_data[i][-1] == 1:
            plt.scatter(train_data[i][0], train_data[i][1], c=u'b')
        else:
            plt.scatter(train_data[i][0], train_data[i][1], c=u'r')

    # 画感知机分类，slope斜率图
    plt.plot(x, -(w[0]*x+b) / w[1], c=u'r')
    plt.show()

if __name__ == '__main__':
    data_path = '../dataset/perception/dataset.txt'
    train_data = generate_data(data_path)
    epoch, eta, var_num, batch_size = 100, 0.1, 2, 20
    p = Perception(var_num)
    p.sgd(train_data, epoch, eta, batch_size)
    plot_data_scatter(train_data, p.get_weight(), p.get_bias())

    # print generate_date()[0]
    # print generate_date()[0][0:-1]
    # var_num = 2
    # p = Perception(var_num)
    # print p.get_current_para()[0]
