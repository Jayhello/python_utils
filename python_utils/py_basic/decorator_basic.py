# _*_ coding:utf-8 _*_

"""
python @ usage example
"""


def hello(fn):
    def wrapper():
        print "hello, %s" % fn.__name__
        fn()
        print 'bye, %s' % fn.__name__
    return wrapper


def do_nothing(fn):
    def wrapper():
        print 'do not exe fn'
    return wrapper


@hello
def foo():
    print 'I am foo'
    # hello, foo
    # I am foo
    # bye, foo


@do_nothing
def foo_nothing():
    print 'I am foo_nothing'
    # do not exe fn


@do_nothing
@hello
def foo_nested():
    print 'I am foo_nested'
    # do not exe fn


@hello
@do_nothing
def foo_nested_v2():
    print 'I am foo_nested_v2'


if __name__ == '__main__':
    # foo()
    # foo_nothing()
    # foo_nested()
    foo_nested_v2()
    pass
