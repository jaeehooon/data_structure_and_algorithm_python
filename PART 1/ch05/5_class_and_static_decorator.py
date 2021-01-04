# 5.3.1 데코레이터 패턴
class A(object):
    _hello = True       # 클래스 변수

    def foo(self, x):
        print("foo ({0}, {1}) 실행".format(self, x))

    @classmethod
    def class_foo(cls, x):
        print("class foo ({0}, {1}) 실행: {2}".format(cls, x, cls._hello))

    @staticmethod
    def static_foo(x):
        print("static_foo ({0}) 실행".format(x))


if __name__ == '__main__':
    a = A()
    a.foo(1)
    a.class_foo(2)
    A.class_foo(2)
    a.static_foo(3)
    A.static_foo(3)
