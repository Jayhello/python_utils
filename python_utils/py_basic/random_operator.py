# _*_ coding:utf-8 _*_
import random, string


def generate_random_num_str(length):
    return ''.join(random.choice(string.letters) for i in range(length))


if __name__ == '__main__':
    print random.choice(string.letters)
    print generate_random_num_str(5)
    print string.letters
    pass

