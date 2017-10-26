# _*_ coding:utf-8 _*_


def inc(x):
    def inc_x(y):
        return x + y
    return inc_x


def test_inc():
    inc2 = inc(2)
    inc5 = inc(5)

    print inc2(5)  # 7
    print inc5(5)  # 10

if __name__ == '__main__':
    test_inc()
    pass
