# 1.7.4 피보나치 수열
# 제너레이터 활용


def fib_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


if __name__ == '__main__':
    fg = fib_generator()
    for _ in range(10):
        print(next(fg), end=" ")
