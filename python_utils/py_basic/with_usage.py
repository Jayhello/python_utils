# _*_ coding:utf-8 _*_


class Sample(object):
    def __enter__(self):
        print 'in __enter__'
        return "Foo"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'in __exit__'


def get_sample():
    return Sample()


def test_with():
    with get_sample() as sp:
        print 'Sample: ', sp

if __name__ == '__main__':
    test_with()
    pass
