# _*_ coding:utf-8 _*_
import numpy as np
from utils.FileUtil import get_line_lst


class PcaClass(object):
    def __init__(self):
        pass

    def pca(self, arr_data):
        mean_value = np.mean(arr_data, axis=0)


def load_data():
    file = '../dataset/pca/pca_data.txt'
    lst_row = get_line_lst(file)

    arr_data = np.array([[float(item)for item in row.split()] for row in lst_row]);

    return arr_data

if __name__ == '__main__':
    load_data()
    pass
