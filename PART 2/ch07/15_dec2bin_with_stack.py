# 7.7 연습문제
# 7.7.1 스택 - 괄호의 짝 확인하기
from stack_ import Stack


def dec2bin_with_stack(decNum):
    s = Stack()
    str_aux = ""

    while decNum > 0:
        dig = decNum % 2
        decNum //= 2
        s.push(dig)

    while not s.isEmpty():
        str_aux += str(s.pop())

    return str_aux


if __name__ == '__main__':
    decNum = 9
    print(dec2bin_with_stack(decNum))
