# _*_ coding:utf-8 _*_

"""
This file is about approaches of operating list in python.
Like some concise way, avoiding intricate for loop
"""


def lst_condition():
    lst = [0, 1, 0, 3]
    print [a if a else 2 for a in lst]  # change 0 -> 2
    # [2, 1, 2, 3]
    print ["ha" if i else "Ha" for i in range(3)]
    # ['Ha', 'ha', 'ha']

    # print [i if i % 2 for i in range(4)]
    # ['Ha', 'ha', 'ha']


def lst_shift():
    """
    a basic way of shift list
    :return:
    """
    lst = [1, 2, 3, 4]
    shift_n = 2
    print lst[shift_n:] + lst[:shift_n]
    # [3, 4, 1, 2]
    shift_n = 1
    print lst[shift_n:] + lst[:shift_n]
    # [2, 3, 4, 1]

    lst = [1, 2, 3, 4]
    lst.append(lst.pop(0))
    print lst
    # [2, 3, 4, 1]


def lst_shift_efficient():
    """
    a efficient way of shift list
    :return:
    """
    from collections import deque
    de_lst = deque([1, 2, 3, 4])
    de_lst.rotate(1)
    print de_lst
    # deque([4, 1, 2, 3])


def del_col_in_2dlst():
    """
    remove certain col in 2-d list
    :return:
    """
    td_lst = [[1, 2, 3], [1, 2, 3]]
    print [lst[1:] for lst in td_lst]
    # [[2, 3], [2, 3]]


def range_xrange():
    print range(0, 3)
    # [0, 1, 2]
    print range(3)
    # [0, 1, 2]
    print range(0, 7, 2)
    # [0, 2, 4, 6]
    print xrange(0, 3)
    # xrange(3)
    for i in xrange(3):
        print i  # 0 1 2


def lst_self_step():
    # L[start:stop:step]
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in lst[::2]:
        print i
        # 1 3 5 7 9

    for i in lst[1::2]:
        print i
        # 2 4 6 8 10


def lst_reverse():
    lst = [1, 2, 3, 4, 5, 6]
    print lst[::-1]
    # [6, 5, 4, 3, 2, 1]
    print lst[::-2]
    # [6, 4, 2]

    lst = [1, 2, 3, 4, 5, 6, 7]
    print lst[:-1]
    # [1, 2, 3, 4, 5, 6]
    print lst[:-3]
    # [1, 2, 3, 4]
    print lst[:-3:-1]
    # [7, 6]
    print lst[:-3:1]
    # [1, 2, 3, 4]
    # is step is minus, firstly we reverse the lst and then get the lst by step
    print lst[:3:-1]
    # [7, 6, 5]
    print lst[:-1:-1]
    # []
    print lst[:-2:-1]
    # [7]

    # =======================
    # [1, 2, 3, 4, 5, 6, 7]
    #  0  1  2  3  4  5  6
    # -7 -6 -5 -4 -3 -2 -1
    print lst[-7:-1]
    # [1, 2, 3, 4, 5, 6]
    print lst[-7:0]
    # []
    print lst[-7:]
    # [1, 2, 3, 4, 5, 6, 7]
    print lst[-5:-2]
    # [3, 4, 5]


def generate_range_tuple_list(start, end, step):
    """
    for example generate_range_tuple_list(0, 11, 5) ->
     [(0, 5), (5, 10), (10, 11)]
    :param start:  for eg 0
    :param end:    for eg 11
    :param step:   for eg 5
    :return: [(0, 5), (5, 10), (10, 11)]
    """
    ret_lst = []
    for i in xrange(start, end, step):
        tp = (i, i + step if(i + step < end) else end)
        ret_lst.append(tp)

    return ret_lst


def create_list_repeated_n_times():
    # generate list with 10 0
    lst_i = [0 for i in xrange(10)]
    print lst_i
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    lst_i_2 = [0] * 3
    print lst_i_2
    # [0, 0, 0]

    lst_d = [lst_i_2] * 3
    print lst_d
    # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    lst_d[0].append(0)
    print lst_d
    # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def sort_lst_by_item():
    """
    for example lst = ['F:/0.jpg', 'F:/1.jpg', ..., 'F:/101.jpg']
    in the directory, when we read it.They are sorted by str not the num in pig name
    we want to read it like that:
    F:/0.jpg F:/1.jpg F:/9.jpg F:/10.jpg
    not
    F:/0.jpg F:/10.jpg F:/9.jpg
    :return:
    """
    import glob
    import os
    img_dir = 'F:/ad_samples/img_voice_test/tencent_img/tencent_ocr_sample/'

    lst = glob.glob(img_dir + "*.jpg")
    # os.path.splitext(x)[0].split('\\')[-1] get num '9' from F:/9.jpg
    lst_sorted = sorted(lst, key=lambda x: int(os.path.splitext(x)[0].split('\\')[-1]))
    return lst_sorted


def clear_lst():
    """
    method to clear a list
    Python 3.3+ you can also use list.clear()
    """
    a = [1, 2, 3]
    b = a
    a = []
    print a  # []
    print b  # [1, 2, 3]

    a = [1, 2, 3]
    b = a
    del a[:]  # equivalent to   del a[0:len(a)]
    print a  # []
    print b  # []


def eu_distance():
    a1 = [1, 2, 3]
    a2 = [3, 4, 5]
    from math import sqrt
    print sqrt(sum((a - b)**2 for a, b in zip(a1, a2)))
    # 3.46410161514


def lst_tuple_column():
    lst_tp = [('33', 1), ('88', 2), ('22', 3), ('44', 4)]
    # 2 column
    print [x[1] for x in lst_tp]
    # [1, 2, 3, 4]
    print sum(x[1] for x in lst_tp)
    # 10
    from operator import itemgetter
    print map(itemgetter(1), lst_tp)
    # [1, 2, 3, 4]
    print map(lambda x: x[1], lst_tp)
    # [1, 2, 3, 4]
    print dict(lst_tp).keys()
    # ['33', '88', '44', '22']
    print dict(lst_tp).values()
    # [1, 2, 4, 3]


def lst_counter():
    print [1, 2, 3, 4, 1, 4, 1].count(1)
    # 3
    from collections import Counter
    z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
    print Counter(z)
    # Counter({'blue': 3, 'red': 2, 'yellow': 1})

    lst = ["a", "b", "b"]
    print [[x, lst.count(x)] for x in set(lst)]
    # [['a', 1], ['b', 2]]

    print dict((x, lst.count(x)) for x in set(lst))
    # {'a': 1, 'b': 2}

    print dict((i, lst.count(i)) for i in lst)
    # {'a': 1, 'b': 2}


def get_max_val_idx():
    lst = [1, 7, 3, 5, 6]
    max_val = max(lst)
    print max_val
    # 7
    max_idx = lst.index(max_val)
    print max_idx
    # 1

    import operator
    index, value = max(enumerate(lst), key=operator.itemgetter(1))
    print index, value
    # 1 7


def get_all_idx_of_val():
    lst = [1, 2, 1, 3, 1, 4]
    val = 1
    # print [idx if v == val for idx, v in enumerate(lst)]
    print [idx for idx, v in enumerate(lst) if v == val]
    # [0, 2, 4]

    import numpy as np
    arr = np.array(lst)
    print np.where(arr==val)
    # (array([0, 2, 4], dtype=int64),)
    print np.where(arr==val)[0]
    # [0 2 4]


def max_activity():
    """
    sorting, by the difference in two elements of a tuple
    https://stackoverflow.com/questions/8982900/python-custom-sorting-by-the-difference-in-two-elements-of-a-tuple
    """
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2]
    e = [4, 5, 6, 7, 4, 6, 9, 10, 11, 5]

    tp_lst = zip(s, e)
    print tp_lst
    # [(1, 4), (3, 5), (0, 6), (5, 7), (3, 4), (5, 6), (6, 9), (8, 10), (8, 11), (2, 5)]

    tp_lst.sort(key=lambda t: t[1] - t[0])
    print tp_lst
    # [(3, 4), (5, 6), (3, 5), (5, 7), (8, 10), (1, 4), (6, 9), (8, 11), (2, 5), (0, 6)]

    lst = sorted(zip(s, e), key=lambda t: t[1]-t[0])
    print lst
    # [(3, 4), (5, 6), (3, 5), (5, 7), (8, 10), (1, 4), (6, 9), (8, 11), (2, 5), (0, 6)]

    print sorted(zip(s, e), key=lambda t: t[1]-t[0], reverse=True)
    # [(0, 6), (1, 4), (6, 9), (8, 11), (2, 5), (3, 5), (5, 7), (8, 10), (3, 4), (5, 6)]


def remove_item_while_iter():
    lst = [1, 1, 0, 2, 0, 0, 8, 3, 0]

    print filter(lambda x: x != 0, lst)
    # [1, 1, 2, 8, 3]

    print [x for x in lst if x != 0]
    # [1, 1, 2, 8, 3]

    for item in lst[:]:
        if item == 0:
            lst.remove(item)

    print lst
    # [1, 1, 2, 8, 3]

    lst = [1, 1, 0, 2, 0, 0, 8, 3, 0]

    while 0 in lst:
        lst.remove(0)
    print lst
    # [1, 1, 2, 8, 3]


def test_print():
    tp_lst = [(0, 1), (2, 3), (4, 5)]

    for item in tp_lst: print item

    print "->".join([str(item) for item in tp_lst])
    # (0, 1)->(2, 3)->(4, 5)


def test_find_cond():
    lst = [0.5, 0.3, 0.9, 0.8]

    print filter(lambda x: x[1] > .7, enumerate(lst))
    # [(2, 0.9), (3, 0.8)]
    print next(x[0] for x in enumerate(lst) if x[1] > 0.7)
    # 2
    print [n for n, i in enumerate(lst) if i > 0.7][0]
    # 2

    lst = [0.5, 0.3, 0.9, 0.8, 0.7]
    # find from right
    print next(x[0] for x in enumerate(lst[::-1]) if x[1] < 0.7)
    # 3

    lst = [0.5, 0.3, 0.9, 0.8, 0.7]
    print next(x[0] for x in enumerate(lst[::-1]) if x[1] < 0.3)
    # StopIteration


def test_lst_sum():
    lst = [1, 3, 5]
    print sum(lst)  # 9
    print sum(lst[1:])  # 8

    print sum(lst[5:])  # 0
    print sum(lst[5:-1])  # 0

    print sum(lst[1: -1])  # 3

    lst_tp = [('33', 1), ('88', 2), ('22', 3), ('44', 4)]
    print sum(x[1] for x in lst_tp[1:])  # 9


if __name__ == '__main__':
    test_find_cond()
    # test_lst_sum()
    # test_find_cond()
    # test_print()
    # remove_item_while_iter()
    # get_all_idx_of_val()
    # get_max_val_idx()
    # lst_delete_in_for_loop()
    # lst_counter()
    # lst_tuple_column()
    # eu_distance()
    # lst_reverse()
    # lst_self_step()
    # range_xrange()
    # lst_condition()
    # lst_delete()
    # lst_shift()
    # lst_shift_efficient()
    # del_col_in_2dlst()
    # print generate_range_tuple_list(0, 11, 5)
    # create_list_repeated_n_times()
    # clear_lst()
    pass
