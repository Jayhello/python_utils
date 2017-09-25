# _*_ coding:utf-8 _*_
import random
import string


def generate_random_num_str(length):
    return ''.join(random.choice(string.letters) for i in range(length))


def get_random_int():
    # n -> [0, 10]
    n =random.randint(0, 10)
    print n


def rand_range():
    print random.randrange(1, 100)
    # like 23
    print random.randrange(0, 100, 10)
    # 20
    print random.randrange(0, 100, 10)
    # 90

if __name__ == '__main__':
    rand_range()
    # get_random_int()
    # print random.choice(string.letters)
    # f
    # print generate_random_num_str(5)
    # bjSQU
    # print string.letters
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    pass
