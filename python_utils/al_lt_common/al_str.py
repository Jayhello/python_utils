# coding:utf-8


def max_unique_substr(src):
    LEN = len(src)

    lst_ret = []
    cur_max = 0
    s_tmp = ''
    for i in xrange(LEN):
        if src[i] not in s_tmp:
            s_tmp += src[i]
            cur_max += 1
            if len(lst_ret):
                if len(lst_ret[0]) < cur_max:
                    lst_ret = [s_tmp]
            else:
                lst_ret.append(s_tmp)
        else:
            idx = s_tmp.find(src[i])
            s_tmp = s_tmp[idx + 1:] + src[i]
            cur_max = len(s_tmp)
            if len(lst_ret[0]) == cur_max and s_tmp not in lst_ret:
                lst_ret.append(s_tmp)

    return lst_ret


def max_unique_substr_len(src):
    char_last_idx = [-1] * 256
    b, e, cur_max, max_len = -1, -1, 0, 0

    for i in xrange(len(src)):
        char_idx = ord(src[i])
        last_idx = char_last_idx[char_idx]
        if last_idx == -1 or last_idx > e or last_idx < b:
            char_last_idx[char_idx] = i
            e += 1
            cur_max += 1
            if cur_max > max_len:
                max_len = cur_max
        else:
            e = i
            b = last_idx + 1
            cur_max = e - b + 1
            char_last_idx[char_idx] = i

    return max_len


def test_max_unique_substr():
    s1 = 'abdefgabef'
    print max_unique_substr(s1)
    # ['abdefg', 'bdefga', 'defgab']
    s1 = 'bbbb'
    print max_unique_substr(s1)
    # ['b']
    s1 = 'geeksforgeeks'
    print max_unique_substr(s1)
    # ['eksforg', 'ksforge']
    s1 = 'qwertqwer'
    print max_unique_substr(s1)

    s1 = 'abdefgabef'
    print max_unique_substr_len(s1)

    s1 = 'abcd'
    print max_unique_substr_len(s1)

    s1 = 'bbbb'
    print max_unique_substr_len(s1)

    s1 = 'geeksforgeeks'
    print max_unique_substr_len(s1)

    s1 = 'qwertqwer'
    print max_unique_substr_len(s1)


def print_lst_str(lst_s):
    print "".join(lst_s)


def str_permute(lst_s, b, e):
    if b == e:
        print_lst_str(lst_s)

    for i in xrange(b, e + 1):
        lst_s[b], lst_s[i] = lst_s[i], lst_s[b]
        # str_permute(lst_s, i + 1, e)
        str_permute(lst_s, b + 1, e)
        lst_s[i], lst_s[b] = lst_s[b], lst_s[i]


def print_permutation_str(str):
    n, lst_s = len(str), list(str)
    str_permute(lst_s, 0, n - 1)


def test_pps():
    s = 'abc'
    print_permutation_str(s)
    s = 'abcd'
    print_permutation_str(s)


if __name__ == '__main__':
    # test_pps()
    # test_max_unique_substr()

    print list('abc')
    # ['a', 'b', 'c']
    pass
