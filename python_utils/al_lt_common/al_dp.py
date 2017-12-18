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
                if j < lst_weight[i]:
                    ret_lst[i].append(0)
                else:
                    ret_lst[i].append(lst_val[i])
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


def can_jump(lst, n):
    cur_reachable = 0

    for i in xrange(n):
        if cur_reachable < i:
            return False
        cur_reachable = max(cur_reachable, i + lst[i])
        if cur_reachable >= n:
            return True

    return False


def can_jump_v2(lst, n):
    max_reach = 0
    for i in xrange(n):
        if i <= max_reach:
            max_reach = max(max_reach, i + lst[i])
        else:
            break

    return max_reach >= n


def test_can_jump():
    lst = [2, 3, 1, 1, 4]
    print can_jump(lst, 4)
    print can_jump_v2(lst, 4)

    lst = [3, 2, 1, 0, 4]
    print can_jump(lst, 4)
    print can_jump_v2(lst, 4)

    lst = [1, 0, 0, 3, 2]
    print can_jump(lst, 4)
    print can_jump_v2(lst, 4)


# def can_jump2(lst):
#     """https://discuss.leetcode.com/topic/3191/o-n-bfs-solution/8
#         http://bangbingsyb.blogspot.hk/2014/11/leetcode-jump-game-i-ii.html
#     """
#     lst_max_dis = []
#     LEN = len(lst)
#     cur_max = 0
#     for i in xrange(LEN - 1):
#         if cur_max < i:
#             return -1
#         else:
#             cur_max = max(cur_max, i + lst[i])
#             if i == 0:
#                 lst_max_dis.append(cur_max)
#             else:
#                 if cur_max > lst_max_dis[-1]:
#                     lst_max_dis.pop()
#                     lst_max_dis.append(cur_max)
#                     if cur_max >= LEN - 1: break
#
#     print lst_max_dis
#     if max(lst_max_dis) < LEN - 1:
#         return -1
#
#     return filter(lambda x: x[1] >= LEN - 1, enumerate(lst_max_dis))[0][0] + 1


def can_jump2(lst):
    n = len(lst)
    cur_max, last_max, steps, i = 0, 0, 0, 0

    while cur_max < n - 1:
        last_max = cur_max
        while i <= last_max:
            cur_max = max(cur_max, i + lst[i])
            i += 1
        steps += 1
        if cur_max == last_max:
            return -1

    return steps


def test_can_jump2():
    lst = [3, 2, 1, 0, 4]
    print can_jump2(lst)

    lst = [2, 3, 1, 1, 4]
    print can_jump2(lst)

    lst = [1, 0, 0, 3, 4]
    print can_jump2(lst)

    lst = [1, 2]
    print can_jump2(lst)

    lst = [2, 1]
    print can_jump2(lst)

    lst = [1, 2, 1, 1, 1]
    print can_jump2(lst)

    lst = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
    print can_jump2(lst)


if __name__ == '__main__':
    test_can_jump2()
    # test_can_jump()
    # test_knapsack_01()
    # test_climb_stair()
    pass
