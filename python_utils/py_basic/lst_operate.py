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


if __name__ == '__main__':
    lst_reverse()
    # lst_self_step()
    # range_xrange()
    # lst_condition()
    # lst_delete()
    # lst_shift()
    # lst_shift_efficient()
    # del_col_in_2dlst()
    pass
