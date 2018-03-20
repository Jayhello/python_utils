# coding:utf-8

import numpy as np
import operator


def trap_max(lst):
    n = len(lst)
    if n < 2: return 0

    trap, lst_tmp = 0, [(0, lst[0])]

    for i in xrange(1, n):
        if 0 != lst[i]:
            lst_tmp.append((i, lst[i]))

        if lst[i] >= lst_tmp[0][1]:
            h = min(lst_tmp[0][1], lst_tmp[-1][1])
            w = lst_tmp[-1][0] - lst_tmp[0][0] - 1
            area = h * w
            vault = sum(x[1] for x in lst_tmp[1: -1])
            trap = trap + area - vault
            lst_tmp = lst_tmp[-1:]

    while len(lst_tmp) > 1:
        v = lst_tmp[-1][1]
        idx = next(x[0] for x in enumerate(lst_tmp[::-1]) if x[1][1] > v)
        idx = len(lst_tmp) - idx - 1

        h = min(lst_tmp[idx][1], lst_tmp[-1][1])
        w = lst_tmp[-1][0] - lst_tmp[idx][0] - 1
        area = h * w
        vault = sum(x[1] for x in lst_tmp[idx + 1: -1])
        trap = trap + area - vault
        lst_tmp = lst_tmp[: idx + 1]

    return trap


def test_trap_max():
    lst = [3, 0, 4]
    print trap_max(lst)

    lst = [2, 0, 2]
    print trap_max(lst)

    lst = [4, 6]
    print trap_max(lst)

    lst = [4, 6, 8]
    print trap_max(lst)

    lst = [5, 0, 2, 6]
    print trap_max(lst)

    lst = [7, 0, 6, 0, 5]
    print trap_max(lst)

    lst = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print trap_max(lst)

    lst = [3, 0, 0, 2, 0, 4]
    print trap_max(lst)


def longest_consecutive(lst):
    n, d_map = len(lst), {}
    if n == 0:return 0

    for item in lst: d_map[item] = False

    n_ret = 0
    for num in d_map.iterkeys():
        if d_map[num]: continue

        val, count = num, 0
        while val in d_map:
            count += 1
            d_map[val] = True
            val += 1

        n_ret = max(n_ret, count)

    return n_ret


def test_lc():
    lst = [100, 4, 200, 1, 3, 2]
    print longest_consecutive(lst)


def remove_duplicate(lst):
    i, j, n = 0, 1, len(lst)
    if 0 == n or 1 == n: return n

    while j < n:
        if lst[j] != lst[j - 1]:
            i += 1
            lst[i] = lst[j]
        j += 1

    # lst = lst[: i + 1]  does't change lst
    # for k in xrange(i + 1, n): lst.pop(k) bug for lst size change
    for k in xrange(i + 1, n): lst.pop(-1)

    return i + 1


def test_rd():
    lst = [1, 2, 2, 3]
    print remove_duplicate(lst), lst

    lst = [1, 2, 3]
    print remove_duplicate(lst), lst

    lst = [2, 2, 2, 2]
    print remove_duplicate(lst), lst

    lst = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    print remove_duplicate(lst), lst


def remove_duplicate_2(lst):
    n = len(lst)
    if n < 3: return n

    i, j, flag = 0, 1, 1
    while j < n:
        if lst[j] == lst[j - 1] and 1 == flag:
            i, flag = i + 1, 2
            lst[i] = lst[j]
        elif lst[j] != lst[j - 1]:
            i, flag = i + 1, 1
            lst[i] = lst[j]

        j += 1

    for k in xrange(i + 1, n):lst.pop(-1)

    return i + 1


def remove_duplicate_3(lst):
    n = len(lst)
    if n < 3: return n

    i, j = 2, 2
    while j < n:
        if lst[j] != lst[i - 2]:  # i - 2 not j - 2
            lst[i] = lst[j]
            i += 1
        j += 1

    for k in xrange(i, n): lst.pop(-1)  # not i + 1

    return i    # not i + 1


def test_rd_2():
    lst = [1, 1, 1, 2, 2, 3]
    print remove_duplicate_3(lst), lst

    lst = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3]
    print remove_duplicate_3(lst), lst

    lst = [1, 1, 1, 2, 2, 3]
    print remove_duplicate_3(lst), lst


def search_rotate_sorted(lst, val):
    n = len(lst)
    b, e = 0, n - 1
    while b <= e:
        mid = (b + e) / 2
        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            if lst[mid] <= lst[e]:
                if lst[e] >= val:b = mid + 1
                else: e = mid - 1
            else:
                b = mid + 1
        elif lst[mid] >= val:
            if lst[mid] <= lst[e]:
                e = mid - 1
            else:
                if val >= lst[b]:e = mid - 1  # >= not >
                else: b = mid + 1

    return -1


def test_srs():
    lst = [4, 5, 6, 7, 7, 8, 0, 1, 2, 2, 3]
    val = 6
    print search_rotate_sorted(lst, val)

    val, lst = 3, [1, 1, 3, 1]
    print search_rotate_sorted(lst, val)

    val, lst = 3, [3, 5, 1]
    print search_rotate_sorted(lst, val)


def median_of_2lst(lst1, lst2):
    len1, len2 = len(lst1), len(lst2)

    i, j, lst = 0, 0, []

    while i < len1 and j < len2:
        if lst1[i] <= lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1

    while i < len1:
        lst.append(lst1[i])
        i += 1

    while j < len2:
        lst.append(lst2[j])
        j += 1

    n = len1 + len2

    if n == 0: return 0

    if n % 2 == 1:
        return lst[n / 2]
    else:
        return (lst[n / 2] + lst[n / 2 - 1]) / 2.0


def test_mo2():
    lst1, lst2 = [1, 3], [2]
    print median_of_2lst(lst1, lst2)

    lst1, lst2 = [1, 3], [2, 4]
    print median_of_2lst(lst1, lst2)


# def two_sum(lst, val):
#     n = len(lst)
#     if n < 2:return None
#
#     lst.sort()
#     i, j = 0, n - 1
#     while i < j:
#         tmp = lst[i] + lst[j]
#         if tmp == val: return [i, j]
#         elif tmp > val: j -= 1
#         else: i += 1
#
#     return None


def two_sum(lst, val):
    n = len(lst)
    if n < 2:return None

    lst = [(i, v) for i, v in enumerate(lst)]
    lst.sort(key=lambda t: t[1])

    i, j = 0, n - 1
    while i < j :
        tmp = lst[i][1] + lst[j][1]

        if tmp == val: return [lst[i][0], lst[j][0]]
        elif tmp > val: j -= 1
        else: i += 1

    return None


def test_ts():
    lst, val = [2, 11, 7, 15], 9
    print two_sum(lst, val)
    pass


def three_sum(lst):
    def find_2(lst, val, idx):
        n = len(lst)
        i, j, ret_lst = 0, n - 1, []
        while i < j:
            if i == idx:i += 1
            if j == idx:j -= 1

            tmp = -(lst[i] + lst[j])
            if tmp == val:
                ret_lst.append([lst[i], lst[j], val])
                j -= 1
            elif -tmp > val: j -= 1
            else: i += 1

        return ret_lst

    # lst = sorted(set(lst))
    lst.sort()
    n = len(lst)
    if n < 3: return None

    ret_lst = []
    set_visited = set()
    for i, v in enumerate(lst):
        if v not in set_visited:
            ret = find_2(lst, v, i)
            if len(ret):
                ret_lst += ret
            set_visited.add(v)

    return ret_lst


def test_3sum():
    lst = [-1, 0, 1, 2, -1, -4]
    print three_sum(lst)


def sum3_closest(lst, val):
    n = len(lst)
    if n < 3: return None

    def find_closest(lst, idx, val):
        pass

    m_close = lst[0] + lst[1] + lst[2]
    for i, v in enumerate(lst):
        tmp = v - val
        ret = find_closest(lst, i, tmp)
        m_close = min(m_close, ret)

    return m_close


def test_s3c():
    lst, val = [-1, 2, 1, -4], 1
    print sum3_closest(lst, val)


def remove_ele(lst, val):
    n, j = len(lst), 0

    for i in xrange(n):
        if lst[i] != val:
            lst[j] = lst[i]
            j += 1

    return j


def test_re():
    lst, val = [3, 5, 4, 5, 3], 5
    print remove_ele(lst, val), lst
    # 3 [3, 4, 3, 5, 3]


def lexi_next_permutation(lst_s):
    n = len(lst_s)
    i = n - 2

    while i >= 0 and lst_s[i] >= lst_s[i + 1]:
        i -= 1

    if i < 0:
        return ''.join(lst_s)

    j = n - 1
    while lst_s[j] <= lst_s[i]:  # <= not <
        j -= 1

    lst_s[i], lst_s[j] = lst_s[j], lst_s[i]
    lst_s[i + 1:] = lst_s[n - 1: i :-1]

    return ''.join(lst_s)


def lnp(s):
    lst_s = list(s)
    return lexi_next_permutation(lst_s)


def test_lnp():
    s = '2431'
    print lnp(s)  # 3124

    s = '0125330'
    print lnp(s)  # 0130235

    s = '151'
    print lnp(s)  # 511


def check(ch, lst_b):
    if ch == '.': return True
    if lst_b[int(ch) - 1]:return False

    lst_b[int(ch) - 1] = True
    return True


def valid_sd(board):
    for i in xrange(9):
        lst_b = [False] * 9
        for j in xrange(9):  # check row
            if not check(board[i][j], lst_b):
                return False

        lst_b = [False] * 9
        for j in xrange(9):  # check column
            if not check(board[j][i], lst_b):
                return False
    # check sub 9 board(3 rows, 3 columns)
    for r in xrange(3):
        for c in xrange(3):
            lst_b = [False] * 9

            for i in xrange(3):
                r_idx = r * 3 + i  # every sub board row index
                for j in xrange(3):
                    c_idx = c * 3 + j  # every sub board column index
                    if not check(board[r_idx][c_idx], lst_b):
                        return False

    return True


def rotate_mat(lst2):
    n = len(lst2)

    for i in xrange(n / 2):  # 遍历每一层
        m = n - 1 - i        # 每一层的边界
        for j in xrange(i, m):  # 替换选择四个点
            tmp = lst2[i][j]
            lst2[i][j] = lst2[n - j - 1][i]
            lst2[n - j - 1][i] = lst2[n - i - 1][n - j - 1]
            lst2[n - i - 1][n - j - 1] = lst2[j][n - 1 - i]
            lst2[j][n - 1 - i] = tmp


def test_rm():
    lst = np.arange(25).reshape(5, 5)
    rotate_mat(lst)
    print lst


def lst_add1(lst):
    n, carry = len(lst), 1

    for i in reversed(xrange(n)):
        r = lst[i] + carry
        if r > 9:
            r %= 10
            lst[i] = r
        else:
            lst[i] = r
            carry = 0
            break
    if carry == 1:
        lst.insert(0, 1)

    return lst


def lst_add1_v2(lst):
    n = len(lst)

    for i in reversed(xrange(n)):
        if lst[i] == 9: lst[i] = 0
        else:
            lst[i] += 1
            return lst

    if lst[-1] == 0: lst.insert(0, 1)

    return lst


def test_la1():
    lst = [9, 9, 9]
    # print lst_add1(lst)
    print lst_add1_v2(lst)


def gray_code(n):
    lst = [0]
    high_or = 1
    for i in xrange(n):
        for j in reversed(xrange(len(lst))):
            lst.append(lst[j] | high_or)

        high_or <<= 1

    return lst


def gray_code_v2(n):
    lst = [0]
    for i in xrange(n):
        for j in reversed(xrange(len(lst))):
            lst.append(lst[j] | (1 << i))

    return lst


def test_gc():
    print gray_code_v2(2)
    print gray_code_v2(3)
    print gray_code_v2(4)


def set_mat_zero(lst2):
    m, n = len(lst2), len(lst2[0])

    b_r_zero, b_c_zero = False, False

    for i in xrange(n):  # check first row will be 0
        if lst2[0][i] == 0:
            b_r_zero = True
            break

    for j in xrange(m):  # check first column will be 0
        if lst2[j][0] == 0:
            b_c_zero = True
            break

    for i in xrange(1, m):
        for j in xrange(1, n):
            if lst2[i][j] == 0:
                lst2[0][j] = 0
                lst2[i][0] = 0

    for i in xrange(1, m):
        if lst2[i][0] == 0:
            for j in xrange(1, n):
                lst2[i][j] = 0

    for j in xrange(1, n):
        if lst2[0][j] == 0:
            for i in xrange(1, m):
                lst2[i][j] = 0

    if b_r_zero:
        for j in xrange(n):
            lst2[0][j] = 0

    if b_c_zero:
        for i in xrange(m):
            lst2[i][0] = 0


def test_smz():
    lst = [[0, 1, 1, 0], [1, 0, 1, 1],
           [1, 1, 1, 1], [0, 1, 1, 1]]

    set_mat_zero(lst)
    print lst


def gas_station(lst_gas, lst_cost):
    n = len(lst_gas)

    for i in xrange(n):
        cur, flag = 0, True
        for j in xrange(i, n):
            cur += lst_gas[j]
            cur -= lst_cost[j]
            if cur < 0:  # 这里必须加上这个判断
                flag = False
                break

        if flag:  # 如果可以继续
            for j in xrange(0, i):  # 循环
                cur += lst_gas[j]
                cur -= lst_cost[j]
                if cur < 0: break

        # 还有剩余的油
        if cur >= 0: return i

    return -1


def gas_station_v2(lst_gas, lst_cost):
    n = len(lst_gas)

    for i in xrange(n):
        store = lst_gas[i]
        j = i
        while store >= lst_cost[j]:
            store -= lst_cost[j]
            j = (j + 1) % n  # % n not % i

            if j == i: return i  # 回到原来的点

            store += lst_gas[j]

    return -1


def gas_station_v3(lst_gas, lst_cost):
    # merge to the below for loop
    # if sum(lst_gas) < sum(lst_cost): return -1

    n, store, idx, gap = len(lst_gas), 0, 0, 0

    for i in xrange(n):
        gap = gap + lst_gas[i] - lst_cost[i]
        store += lst_gas[i]
        store -= lst_cost[i]
        if store < 0:
            idx = i + 1
            store = 0

    if gap < 0: return -1
    return idx


def test_gs():
    # lst1, lst2 = [3, 1, 2, 5, 4], [4, 1, 1, 2, 3]
    # lst1, lst2 = [1, 2, 3, 4], [1, 2, 3, 4]
    lst1, lst2 = [2, 4], [3, 4]
    # print gas_station(lst1, lst2)
    # print gas_station_v2(lst1, lst2)
    print gas_station_v3(lst1, lst2)
    pass


def candy_num(lst):
    n = len(lst)
    lst_num = [1] * n

    for i in xrange(n - 1):  # better than 1, n
        if lst[i + 1] > lst[i]:
            # lst_num[i] += 1 比前一个大1，而不是自己加 1
            lst_num[i + 1] = lst_num[i] + 1

    for i in reversed(xrange(n - 1)):
        # if lst[i + 1] < lst[i] and lst_num[i - 1] <= lst_num[i]:
        if lst[i + 1] < lst[i]:
            lst_num[i] = max(lst_num[i], lst_num[i + 1] + 1)

    return sum(lst_num), lst_num


def test_cn():
    lst1, lst2, lst3 = [1, 3, 2, 1], [1, 3, 5], [1, 0, 2]
    print candy_num(lst1)  # (7, [1, 3, 2, 1])
    print candy_num(lst2)  # (6, [1, 2, 3])
    print candy_num(lst3)  # (5, [2, 1, 2])


def single_num(lst):
    n, ret = len(lst), 0
    for i in xrange(n):
        ret ^= lst[i]

    return ret


def single_num_v2(lst):
    ret = 0
    for num in lst:
        ret ^= num

    return ret


def single_num_v3(lst):
    return reduce(lambda x, y: x^y, lst)


def single_num_v4(lst):
    return reduce(operator.xor, lst)


def test_sn():
    lst = [3, 3, 5]
    # print single_num(lst)
    # print single_num_v2(lst)
    print single_num_v3(lst)
    print single_num_v4(lst)


def find_right_bit1(num):
    idx = 0
    while (num & 1 == 0) and idx < 32:
        num, idx = num >> 1, idx + 1

    return idx


def is_nth_bit1(num, idx):
    while idx:
        num >>= 1
        idx -= 1

    return num & 1


def single_num2(lst):
    xor_ret = 0
    for n in lst:
        xor_ret ^= n

    idx = find_right_bit1(xor_ret)

    ret1, ret2 = 0, 0
    for n in lst:
        if is_nth_bit1(n, idx):
            ret1 ^= n
        else:
            ret2 ^= n

    return ret1, ret2


def test_sn2():
    lst = [1, 1, 3, 2, 5, 2]
    print single_num2(lst)

    lst = [1, 1, 3, 0, 5, 0]
    print single_num2(lst)


def single_num3(lst):
    n, ret = len(lst), 0
    for i in xrange(31, -1, -1):
        mask, s = 1 << i, 0
        for j in xrange(n):
            if lst[j] & mask:
                s += 1

        ret = (ret << 1) + (s % 3)

    return ret


def test_sn3():
    lst = [1, 1, 2, 1, 3, 3, 3]
    print single_num3(lst)


def int2roman(n):
    lst_v = [1000, 900, 500, 400, 100,   90,  50,   40,  10,   9,   5,    4,   1]
    lst_s = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    LEN = len(lst_v)

    s_ret = ''
    for i in xrange(LEN):
        while n >= lst_v[i]:
            n -= lst_v[i]
            s_ret += lst_s[i]

    return s_ret


def test_i2r():
    n = 3978
    print int2roman(n)


def roman2int(s_roman):
    lst_s = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    lst_v = [1000, 900, 500, 400, 100,   90,  50,   40,  10,   9,   5,    4,   1]

    s_len, lst_len = len(s_roman), len(lst_s)
    i, j, i_ret = 0, 0, 0

    while i < s_len and j < lst_len:
        s_sub = lst_s[j]
        if s_sub == s_roman[i:i+len(s_sub)]:
            i_ret += lst_v[j]
            i += len(s_sub)
        else:
            j += 1

    return i_ret


def test_r2i():
    s = 'MMMCMLXXVIII'
    print roman2int(s)  # 3978


def subsets(lst):
    lst.sort()
    lst2_ret = []

    for item in lst:
        lst_tmp = []
        # get sets that are already in result
        for lst_item in lst2_ret:
            # lst_tmp.append(lst_item) # shallow copy
            lst_tmp.append(list(lst_item))  # deep copy

        # add S[i] to existing sets
        for lst_item in lst_tmp:
            lst_item.append(item)

        # add S[i] only as a set
        lst_tmp.append([item])

        for lst_item in lst_tmp:
            lst2_ret.append(lst_item)

    lst2_ret.append([])

    return lst2_ret


def test_subsets():
    lst = [1, 2, 3]
    print subsets(lst)
    # [[1], [1, 2], [2], [1, 3], [1, 2, 3], [2, 3], [3], []]


def triangle(lst2):
    row = len(lst2)
    if row < 0: return 0

    dp = [i for i in lst2[row - 1]]

    for r in reversed(xrange(row - 1)):
        for col in xrange(r + 1):
            dp[col] = lst2[r][col] + min(dp[col], dp[col + 1])

    return dp[0]


def test_triangle():
    lst2 = [[-1], [2, 3], [1, -1, -3], [5, 3, -1, 2]]
    print triangle(lst2)


if __name__ == '__main__':
    test_triangle()
    # test_subsets()
    # test_i2r()
    # test_r2i()

    # s = 'abcd'
    # print s[3:2:-1], s[3:1:-1], s[1:0:-1], s[::-1]  # d, dc, b, dcba

    # print 1 << 5, 1 << 31, 1 << 32
    # 32 2147483648 4294967296
    # test_sn3()
    # test_sn2()
    # test_sn()
    # test_cn()
    # test_gs()
    # test_smz()
    # test_gc()
    # test_la1()
    # test_rm()
    # test_lnp()
    # test_re()
    # test_s3c()
    # test_3sum()
    # test_ts()
    # test_mo2()
    # test_srs()
    # test_rd_2()
    # test_rd()
    # test_lc()
    # test_trap_max()
    pass
