# _*_ coding:utf-8 _*_

import numpy as np


def arr_equal():
    ar1 = np.array([[1, 2], [3, 4]])
    ar2 = np.array([[1, 2], [3, 4]])
    ar3 = np.array([[1, 2], [3, 5]])

    print np.array_equal(ar1, ar2)
    # True
    print np.array_equal(ar1, ar3)
    # False


def arr_equiv():
    ar1 = np.array([[1, 2], [3, 4]])
    ar2 = np.array([[1, 2]])
    ar3 = np.array([[1, 2], [1, 2]])
    ar4 = np.array([1, 2])
    print np.array_equiv(ar1, ar2)
    # False
    print np.array_equiv(ar1, ar4)
    # False
    print np.array_equiv(ar2, ar3)
    # True


def arr_close():
    ar1 = np.array([[1, 2], [3, 4]])
    ar2 = np.array([[1.1, 2.1], [3.1, 4.1]])
    ar3 = np.array([[1.00001, 2.00001], [3.00001, 4.00001]])
    ar4 = np.array([[1.0001, 2.0001], [3.0001, 4.0001]])

    print np.isclose(ar1, ar2)
    # [[False False]
    #  [False False]]
    print np.isclose(ar1, ar3)
    # [[ True  True]
    #  [ True  True]]
    print np.isclose(ar1, ar4)
    # [[False False]
    #  [False False]]
    print np.isclose(ar1, ar4, atol=1.e-4)
    # [[ True  True]
    #  [ True  True]]

    print np.allclose([1e10, 1e-7], [1.00001e10, 1e-8])
    # False
    print np.allclose([1e10, 1e-8], [1.00001e10, 1e-9])
    # True

if __name__ == '__main__':
    arr_close()
    # arr_equal()
    # arr_equiv()
    pass
