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
    # [[11  4  6  1]
    #  [10  0  2  9]
    #  [ 8  7  5  3]]
    arr.sort()
    print 'after sort \n', arr
    # [[ 1  4  6 11]
    #  [ 0  2  9 10]
    #  [ 3  5  7  8]]
    print np.sort(arr)  # the result is as some as arr.sort(),default sort by row
    print np.sort(arr, axis=0)  # sort by column, axis=0 means column
    pass

if __name__ == '__main__':
    # arr_arg_sort()
    arr_sort()
    pass
