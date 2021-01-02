# 5.2.2 다형성
class Symbol(object):
    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    x = Symbol("Py")
    y = Symbol("Py")

    symbols = set()
    symbols.add(x)
    symbols.add(y)

    print(x is y)
    print(x == y)
    print(len(symbols))
