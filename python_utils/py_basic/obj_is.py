# coding:utf-8
import operator


def i_is_check():
    a = 256
    b = 256
    print a is b
    # True
    a1 = 2571111
    b1 = 2571111
    print a1 is b1
    # True


def max_activity(s, e):
    tp_lst = sorted(zip(s, e), key=lambda t: t[1] - t[0])

    lst_target = []
    while len(tp_lst):
        tp_lst.sort(key=lambda t: t[1] - t[0])
        min_se = tp_lst[0]
        lst_target.append(min_se)
        tp_lst.pop(0)

        tp_lst = filter(lambda x: x[1] <= min_se[0] or x[0] >= min_se[1], tp_lst)

    # for item in lst_target: print item

    print "->".join([str(item) for item in lst_target])


def test_max_activity():
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2]
    e = [4, 5, 6, 7, 4, 6, 9, 10, 11, 5]
    max_activity(s, e)
    # (3, 4)->(5, 6)->(8, 10)

    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    e = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    max_activity(s, e)
    # (3, 5)->(5, 7)->(12, 14)->(8, 11)


def coin_question(coin_val, coin_count, money):
    sum = 0
    d_val_count = {}

    for i in range(len(coin_val))[::-1]:
        df = money - sum
        n = df / coin_val[i]
        n = min(coin_count[i], n)
        if n:
            sum = sum + n * coin_val[i]
            d_val_count[coin_val[i]] = n

    return d_val_count


def test_coin_question():
    coin_val = [1, 2, 5, 10, 20, 50, 100]
    coin_count = [3, 0, 2, 1, 0, 3, 5]

    money = 113
    d_val_count = coin_question(coin_val, coin_count, money)
    print d_val_count  # {1: 3, 10: 1, 100: 1}

    money = 272
    d_val_count = coin_question(coin_val, coin_count, money)
    print d_val_count  # {1: 2, 50: 1, 100: 2, 10: 1, 5: 2}

if __name__ == '__main__':
    test_coin_question()
    # test_max_activity()
    # i_is_check()
    lst = [1, 2, 3]
    print range(len(lst))[::-1]
    print lst[::-1]
    pass
