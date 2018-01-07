# coding:utf-8


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

    val = 2
    print search_rotate_sorted(lst, val)

    val = 1
    print search_rotate_sorted(lst, val)

    val, lst = 3, [3, 5, 1]
    print search_rotate_sorted(lst, val)


if __name__ == '__main__':
    test_srs()
    # test_rd_2()
    # test_rd()
    # test_lc()
    # test_trap_max()
    pass
