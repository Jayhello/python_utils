# _*_ coding:utf-8 _*_
import random, string


def generate_random_num_str(length):
    return ''.join(random.choice(string.letters) for i in range(length))


def get_random_int():
    # n -> [0, 10]
    n =random.randint(0, 10)
    print n

if __name__ == '__main__':
    get_random_int()
    print random.choice(string.letters)
    # f
    print generate_random_num_str(5)
    # bjSQU
    print string.letters
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    pass

