# coding:utf-8


def f_135():
    yield 1
    yield 3
    yield 5


def demo_1():
    for val in f_135():
        print val

    # 1 3 5

    generator = f_135()
    print next(generator)
    # 1
    print next(generator)
    # 3
    print next(generator)
    # 5


def fibonacci(n):
    cur = 1
    pre = 0
    count = 0
    while count < n:
        yield cur
        cur, pre = cur + pre, cur
        count += 1


def demo_fib():
    ge_fib = fibonacci(10)
    for i in ge_fib:
        print i, ", "
    # 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55

    ge_fib = fibonacci(5)
    print next(ge_fib)
    # 1
    print next(ge_fib)
    # 1


def read_file(f_path='__init__.py'):
    # read 60 bytes once
    bt_once = 60
    with open(f_path, 'rb') as fmp3:
        data = fmp3.read(bt_once)
        while data:
            yield data
            data = fmp3.read(bt_once)


def demo_read_file():
    for txt in read_file():
        print txt

    # # coding:utf-8
    # if __name__ == '__main__':
    # pass

if __name__ == '__main__':
    # demo_1()
    # demo_fib()
    demo_read_file()
    pass
