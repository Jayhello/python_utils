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


def best_time_sell_stock_1(lst):
    LEN = len(lst)
    if LEN < 2: return 0

    cur_min, max_profit = lst[0], 0
    for i in xrange(1, LEN):
        max_profit = max(max_profit, lst[i] - cur_min)
        cur_min = min(cur_min, lst[i])

    return max_profit


def test_bt_ss_1():
    lst = [10, 18, 26, 31, 4, 53, 69]
    print best_time_sell_stock_1(lst)

    lst = [7, 6, 4, 3, 1]
    print best_time_sell_stock_1(lst)

    lst = [7, 1, 5, 3, 6, 4]
    print best_time_sell_stock_1(lst)


def best_time_sell_stock_2(lst):
    max_profit, LEN = 0, len(lst)
    for i in xrange(1, LEN):
        diff = lst[i] - lst[i - 1]
        if diff > 0:
            max_profit += diff

    return max_profit


def test_test_bt_ss_2():
    lst = [5, 1, 2, 3, 4]
    print best_time_sell_stock_2(lst)  # 3

    lst = [12, 41, 54, 12, 20, 50]
    print best_time_sell_stock_2(lst)  # 80


def best_time_sell_stock_3(prices):
    pass


def best_time_sell_stock_3_v2(prices):
    max_profit, n = 0, len(prices)
    if n < 2: return 0
    if n == 2: return max(0, prices[1] - prices[0])

    for i in xrange(1, n - 1):
        min_val = prices[0]
        local_max_1 = 0
        for j in xrange(1, i + 1):
            min_val = min(min_val, prices[j - 1])
            local_max_1 = max(local_max_1, prices[j] - min_val)

        min_val = prices[i]
        local_max_2 = 0
        for k in xrange(i + 1, n):
            min_val = min(min_val, prices[k - 1])
            local_max_2 = max(local_max_2, prices[k] - min_val)

        max_profit = max(max_profit, local_max_1 + local_max_2)

    return max_profit


def test_bt_ss_3():
    prices = [10, 5]
    # print best_time_sell_stock_3(prices)
    print best_time_sell_stock_3_v2(prices)

    prices = [5, 20]
    # print best_time_sell_stock_3(prices)
    print best_time_sell_stock_3_v2(prices)

    prices = [10, 5, 20]
    # print best_time_sell_stock_3(prices)
    print best_time_sell_stock_3_v2(prices)

    prices = [5, 10, 20]
    # print best_time_sell_stock_3(prices)
    print best_time_sell_stock_3_v2(prices)

    prices = [10, 22, 5, 75, 65, 80]  # 87
    # print best_time_sell_stock_3(prices)
    print best_time_sell_stock_3_v2(prices)

    prices = [2, 30, 15, 10, 8, 25, 80]  # 100
    # print best_time_sell_stock_3(prices)
    print best_time_sell_stock_3_v2(prices)

    prices = [100, 30, 15, 10, 8, 25, 80]  # 72
    # print best_time_sell_stock_3(prices)
    print best_time_sell_stock_3_v2(prices)

    prices = [90, 80, 70, 60, 50]  # 0
    # print best_time_sell_stock_3(prices)
    print best_time_sell_stock_3_v2(prices)


def contain_max_water(lst):
    n = len(lst)
    b, e, max_c = 0, n - 1, 0

    while b < e:
        h = min(lst[b], lst[e])
        max_c = max(max_c, (e - b) * h)

        if lst[b] < lst[e]:
            b += 1
        else:
            e -= 1

    return max_c


def test_contain_max_water():
    lst = [1, 5, 4, 3]
    print contain_max_water(lst)

    lst = [1, 4, 9, 4]
    print contain_max_water(lst)

    lst = [2, 3, 4, 5, 18, 17, 6]
    print contain_max_water(lst)  # 17


def interleaving_str(s1, s2, s3):
    if len(s3) == 0 and (len(s1) != 0 | len(s2) != 0):
        return False

    if len(s3) != 0 and (len(s1) == 0 & len(s2) == 0):
        return False

    if len(s3) == 0 & len(s1) == 0 & len(s2) == 0:
        return True

    b1, b2 = False, False

    if len(s1) > 0 and s1[0] == s3[0]:
        b1 = interleaving_str(s1[1:], s2, s3[1:])
    else:
        if len(s2) > 0 and s2[0] == s3[0]:
            b2 = interleaving_str(s1, s2[1:], s3[1:])

    return b1 | b2


def test_il_str():
    s1, s2, s3 = 'aabcc', 'dbbca', 'aadbbcbcac'
    print interleaving_str(s1, s2, s3)
    s3 = 'aadbbbaccc'
    print interleaving_str(s1, s2, s3)

    s1, s2, s3 = "YX", "X", "XXY"
    print interleaving_str(s1, s2, s3)
    s1 = 'XY'
    print interleaving_str(s1, s2, s3)


if __name__ == '__main__':
    test_il_str()
    # test_contain_max_water()
    # s = 'a'
    # print s[1:]
    # test_bt_ss_3()
    # test_test_bt_ss_2()
    # test_bt_ss_1()
    # test_can_jump2()
    # test_can_jump()
    # test_knapsack_01()
    # test_climb_stair()
    pass
