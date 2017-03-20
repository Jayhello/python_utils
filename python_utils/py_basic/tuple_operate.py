# _*_ coding:utf-8 _*_


def list_2_tuple():
    lst = ['python', 12, True, [1, 2]]
    tp = tuple(lst)
    print tp
    # ('python', 12, True, [1, 2])
    tp = tuple(tuple(item) for item in lst)
    print tp


def tuple_shift_left(tup, n):
    """
    shift tuple over by n indices
    :param tup: like (1,2,3,4)
    :param n: 1
    :return: (2, 3, 4, 1)
    """
    if n < 0:
        raise ValueError('n must be a positive integer')
    if not tup or not n:
        return tup
    n %= len(tup)
    return tup[n:] + tup[:n]

if __name__ == '__main__':
    # list_2_tuple()
    tp = (1, 2, 3, 4)
    # print tuple_shift_left(tp, -1)
    # (2, 3, 4, 1)
    print tuple_shift_left(tp, 5)
    # (2, 3, 4, 1)
