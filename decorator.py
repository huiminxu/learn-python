import functools


def use_logging(level="debug"):
    def decorator(func):
        # 不更改装饰器的名字
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("[%s]%s is running" % (level, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@use_logging()
def decoratorDemo1(name="imooc"):
    print('我被装饰了')


def demo():
    print('我被装饰了')


# 类装饰器
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('class decorator running')
        self._func()
        print('clss decorator ending')


@Foo
def bar():
    print('i am bar')


# python 内置装饰器
#
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score


if __name__ == '__main__':
    print('名称', decoratorDemo1.__name__)
    decoratorDemo1()
    decoratorDemo2 = use_logging(level="info")(demo)
    print(decoratorDemo2.__name__)
    print(decoratorDemo2.__doc__)
    bar()
    s = Student("imooc", '100')
    s.score = 100
    s.name = 1
    print(s.score, s.name)
