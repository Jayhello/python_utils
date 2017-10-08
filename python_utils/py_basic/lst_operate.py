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


def lst_delete_in_for_loop():
    lst = [0, 1, 0, 3]
    for item in lst:
        print item
        lst.remove(item)


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
    # generate list with 20 0
    lst_i = [0 for i in xrange(20)]
    print lst_i
    lst_i_2 = [0] * 20
    print lst_i_2


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

if __name__ == '__main__':
    eu_distance()
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

    l = []
    for it in l:
        print "not non"

    pass
