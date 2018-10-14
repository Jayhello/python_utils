# _*_ coding:utf-8 _*_
import random
import string


def generate_random_num_str(length):
    return ''.join(random.choice(string.letters) for i in range(length))


def get_random_int():
    # n -> [0, 10]
    n = random.randint(0, 10)
    print n

    print random.randint(180, 200)


def rand_range():
    print random.randrange(1, 100)
    # like 23
    print random.randrange(0, 100, 10)
    # 20
    print random.randrange(0, 100, 10)
    # 90


def random_seed():
    sd = 3
    random.seed(sd)
    print "Random number with seed 10 : ", random.random()

    # It will generate same random number(do random.seed(sd) every time before)
    random.seed(sd)
    print "Random number with seed 10 : ", random.random()

    # It will generate same random number
    random.seed(sd)
    print "Random number with seed 10 : ", random.random()

if __name__ == '__main__':
    # random_seed()
    # rand_range()
    # get_random_int()
    # print random.choice(string.letters)
    # f
    # print generate_random_num_str(5)
    # bjSQU
    # print string.letters
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    import time
    t = int(time.time())
    print random.randint(1000000, 100000000)

    print random.choice([1, 3, 5, 7])

    pass
