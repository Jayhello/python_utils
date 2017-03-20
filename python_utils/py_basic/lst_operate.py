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

if __name__ == '__main__':
    lst_condition()
