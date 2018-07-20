# _*_ coding:utf-8 _*_

from functools import partial


def inc(x):
    def inc_x(y):
        return x + y
    return inc_x


def test_inc():
    inc2 = inc(2)
    inc5 = inc(5)

    print inc2(5)  # 7
    print inc5(5)  # 10


def to_upper(item):
    return item.upper()


def map_demo():
    name_lst = ['xy', 'bear fish', 'jay']
    name_len = map(len, name_lst)
    print name_len
    # [2, 9, 3]

    name_upper = map(to_upper, name_lst)
    print name_upper
    # ['XY', 'BEAR FISH', 'JAY']

    name_up = []
    for i in range(len(name_lst)):
        name_up.append(name_lst[i].upper())
    print name_up
    # ['XY', 'BEAR FISH', 'JAY']

    squares = map(lambda x: x * x, range(4))
    print squares
    # [0, 1, 4, 9]

    a = [1, 2, 3, 4]
    b = [17, 12, 11, 10]
    c = [-1, -4, 5, 9]
    print map(lambda x, y: x + y, a, b)
    # [18, 14, 14, 14]
    print map(lambda x, y, z: x + y + z, a, b, c)
    # [17, 10, 19, 23]


def reduce_demo():
    lst = range(1, 6)
    print lst  # [1, 2, 3, 4, 5]
    sum = reduce(lambda x, y: x + y, lst)
    print sum  # 15


def cal_aver():
    lst = range(0, 11)
    positive_num_cnt = 0
    positive_num_sum = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            positive_num_cnt += 1
            positive_num_sum += lst[i]

    average = 0
    if positive_num_cnt > 0:
        average = positive_num_sum / positive_num_cnt

    print average  # 5


def filter_demo():
    lst = range(0, 11)
    odd_lst = filter(lambda x: x % 2, lst)
    print odd_lst  # [1, 3, 5, 7, 9]
    average = reduce(lambda x, y: x + y, odd_lst) / len(odd_lst)
    print average  # 5


def f(a, b, c, d):
    """
    used by function partial_demo as demo
    :param a: int
    :param b: int
    :param c: int
    :param d: int
    :return:
    """
    return a * 1000 + b * 100 + c * 10 + d


def partial_demo():
    # A partial function that calls f with
    # a as 3, b as 1 and c as 4.
    g = partial(f, 3, 1, 4)
    print g(5)  # 3145

    g2 = partial(f, d=4, c=3, b=2)
    print g2(1)  # 1234


if __name__ == '__main__':
    partial_demo()
    # test_inc()
    # map_demo()
    # reduce_demo()
    # filter_demo()
    # cal_aver()
    pass
