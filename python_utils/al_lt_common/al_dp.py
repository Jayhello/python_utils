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
    print climb_stair(3)   # 3
    print climb_stair(5)   # 8
    print climb_stair(80)  # 37889062373143906
    # print climb_stair(-1)
    print climb_stair_v2(3)
    print climb_stair_v2(5)
    print climb_stair_v2(80)

if __name__ == '__main__':
    test_climb_stair()
    pass
