# _*_ coding:utf-8 _*_
import numpy as np
from utils.FileUtil import get_line_lst
import matplotlib.pyplot as plt


class PcaClass(object):
    def __init__(self):
        pass

    def pca(self, arr_data):
        mean_value = np.mean(arr_data, axis=0)
        pass


def load_data():
    file = '../dataset/pca/pca_data.txt'
    lst_row = get_line_lst(file)

    arr_data = np.array([[float(item)for item in row.split()] for row in lst_row])

    return arr_data


def plot_src_data(data):
    # f1 = plt.figure(1)
    # plt.plot(data, 'ro')
    # mt = np.array([[1, 2], [2.6, 3.6]])
    # print data[:, 0], data[:, 0].shape
    # print data[:, 1], data[:, 1].shape
    # x = [1, 2]
    # y = [2.6, 3.6]
    # plt.scatter(x, y)
    # add c='r', or you will get error
    plt.scatter(data[:, 0], data[:, 1], c='r')
    # plt.scatter(data, 'ro')
    plt.show()


if __name__ == '__main__':
    data = load_data()
    # mt = np.array([[3, -1], [-1, 3]])
    # plot_src_data(data)
    pca = PcaClass()
    pca.pca(data)
    pass
