# _*_ coding:utf-8 _*_
import numpy as np


def arr_arg_sort():
    arr = np.random.permutation(3 * 4).reshape(3, 4)
    np.random.shuffle(arr)
    print arr
    arr_sort_idx = np.argsort(arr)  # default sort by row
    print arr_sort_idx
    # print np.array(arr)[arr_sort_idx] # does not apply to mul-dim array
    arr_sort_idx = np.argsort(arr, axis=0)  # sort by column
    print arr_sort_idx
    x = np.array([0, 2, 1])
    print np.argsort(x)
    # [0 2 1] ascending order
    print np.argsort(-x)
    # [1 2 0] descending order

    pass


def arr_sort():
    arr = np.random.permutation(3 * 4).reshape(3, 4)
    print arr
    arr.sort()

    pass

if __name__ == '__main__':
    arr_arg_sort()
    pass
