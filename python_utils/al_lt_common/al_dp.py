# coding:utf-8


def climb_stair(n):
    if n <= 0:
        raise ValueError("n must greater than 0")

    d_n1, d_n2 = 1, 2

    if n == 1: return d_n1
    if n == 2: return d_n2

    ret_steps = 0
    while n >= 3:
        ret_steps = d_n1 + d_n2
        d_n1, d_n2 = d_n2, ret_steps
        n -= 1
    return ret_steps


def climb_stair_v2(n):
    if n < 0: raise ValueError("n must greater than 0")

    lst = [0, 1, 2]

    idx = 3
    while idx <= n:
        s = lst[idx - 1] + lst[idx - 2]
        lst.append(s)
        idx += 1
        # lst[idx - 2], lst[idx - 1] = lst[idx - 1], s  no need

    return lst[n]


def test_climb_stair():
    print climb_stair(3)  # 3
    print climb_stair(5)  # 8
    print climb_stair(80)  # 37889062373143906
    # print climb_stair(-1)
    print climb_stair_v2(3)
    print climb_stair_v2(5)
    print climb_stair_v2(80)


def knapsack_01(lst_val, lst_weight, capacity):
    LEN = len(lst_val)
    ret_lst = []
    for _ in xrange(LEN):
        ret_lst.append(list())

    # try:
    for i in xrange(LEN):
        for j in xrange(1, capacity + 1):
            if 0 == i:
                if j < lst_weight[i]: ret_lst[i].append(0)
                else:ret_lst[i].append(lst_val[i])
            else:
                v1 = ret_lst[i - 1][j - 1]  # note j - 1 not j
                v2 = 0
                if j >= lst_weight[i]:
                    v2 = ret_lst[i - 1][j - lst_weight[i]] + lst_val[i]

                max_v = max(v1, v2)
                ret_lst[i].append(max_v)
    # except Exception as e:
    #     print e, i, j, ret_lst
    #     return
    return ret_lst


def test_knapsack_01():
    lst_weight = [2, 2, 6, 5, 4]
    lst_val = [6, 3, 5, 4, 6]
    capacity = 8
    lst_ret = knapsack_01(lst_val, lst_weight, capacity)
    for lst in lst_ret:
        print lst


if __name__ == '__main__':
    test_knapsack_01()
    # test_climb_stair()
    pass
