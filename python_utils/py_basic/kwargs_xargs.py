# _*_ coding:utf-8 _*_


def print_keyword_args(**kwargs):
    # kwargs is a dict of the keyword args passed to the function
    for key, value in kwargs.iteritems():
        print "%s = %s" % (key, value)


def test_print_keyword_args():
    print_keyword_args(first_name="John", last_name="Doe")
    # first_name = John
    # last_name = Doe

    dic_args = {'first_name': 'Bobby', 'last_name': 'Smith'}
    # print_keyword_args(dic_args)
    # TypeError: print_keyword_args() takes exactly 0 arguments (1 given)
    print_keyword_args(**dic_args)
    # first_name = Bobby
    # last_name = Smith


def print_everything(*args):
    for count, thing in enumerate(args):
        print '{0} -> {1}'.format(count, thing)


def test_print_everything():
    print_everything('apple', 'banana', 'cabbage')
    # 0->apple
    # 1->banana
    # 2->cabbage


def func(required_arg, *args, **kwargs):
    # required_arg is a positional-only parameter.
    print required_arg

    # args is a tuple of positional arguments,
    # because the parameter name has * prepended.
    if args:  # If args is not empty.
        print args

    # kwargs is a dictionary of keyword arguments,
    # because the parameter name has ** prepended.
    if kwargs:  # If kwargs is not empty.
        print kwargs


def test_func():
    func("required argument")
    # required argument
    func("required argument", 1, 2, '3')
    # required argument
    # (1, 2, '3')
    func("required argument", 1, 2, '3', keyword1=4, keyword2="foo")
    # required argument
    # (1, 2, '3')
    # {'keyword2': 'foo', 'keyword1': 4}
    # func()
    # TypeError: func() takes at least 1 argument (0 given)


# kwargs default value
class ExampleClass:
    def __init__(self, **kwargs):
        self.val = kwargs['val']
        self.val2 = kwargs.get('val2')
        self.val3 = kwargs.get('val3', 'default_val3')
        self.val4 = kwargs.pop('val4', 'default_val4')


def default_kwargs(**kwargs):
    options = {
        'option1': 'default_value1',
        'option2': 'default_value2',
        'option3': 'default_value3', }

    options.update(kwargs)
    print options


def test_default_kwargs():
    default_kwargs()
    # {'option2': 'default_value2', 'option3': 'default_value3', 'option1': 'default_value1'}
    default_kwargs(option1='new_value1', option3='new_value3')
    # {'option2': 'default_value2', 'option3': 'new_value3', 'option1': 'new_value1'}

if __name__ == '__main__':
    # test_print_keyword_args()
    # test_print_everything()
    # test_func()
    test_default_kwargs()
    pass
