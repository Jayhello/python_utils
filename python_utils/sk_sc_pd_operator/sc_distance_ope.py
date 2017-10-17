# _*_ coding:utf-8 _*_

from scipy.spatial import distance
import numpy as np


def eu_distance():
    a1 = np.array([1, 2, 3])
    a2 = np.array([3, 4, 5])
    print distance.euclidean(a1, a2)
    # 3.46410161514

if __name__ == '__main__':
    eu_distance()
    pass
