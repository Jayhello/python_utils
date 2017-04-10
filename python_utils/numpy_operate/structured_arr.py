# _*_ coding:utf-8 _*_
import numpy as np


def create_structured_arr():
    dtype = [('name', 'S10'), ('height', float), ('age', int)]
    arr_val = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38),
               ('Galahad', 1.7, 38)]

    arr = np.array(arr_val, dtype=dtype)
    print np.sort(arr, order='height')
    pass


if __name__ == '__main__':
    create_structured_arr()
    pass
