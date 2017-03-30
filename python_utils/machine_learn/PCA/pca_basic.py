# _*_ coding:utf-8 _*_
import numpy as np


def get_eigen_vector():
    mt = np.array([[3, -1], [-1, 3]])
    eig_val, eig_vec = np.linalg.eig(mt)
    print eig_val
    print eig_vec


def get_mean():
    mt = np.array([[3, 1], [-1, 3]])
    m_1 = np.mean(mt[0, :])
    m_2 = np.mean(mt[1, :])
    m = np.mean(mt)
    print m_1
    print m_2
    print m

    c_1 = np.mean(mt[:, 0])
    c_2 = np.mean(mt[:, 1])
    print c_1
    print c_2
    m = np.mean(mt, axis=0)
    # m = np.mean(mt, axis=(0, 1))
    print m

if __name__ == '__main__':
    # get_eigen_vector()
    get_mean()
    pass
