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

if __name__ == '__main__':
    # lst_condition()
    # lst_delete()
    # lst_shift()
    lst_shift_efficient()
