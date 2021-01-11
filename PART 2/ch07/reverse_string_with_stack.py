# 7.7 연습문제
# 7.7.1 스택 - 문자열 반전하기
from stack_ import Stack


def reverse_string_with_stack(str1):
    s = Stack()
    revStr = ""

    for c in str1:
        s.push(c)

    while not s.isEmpty():
        revStr += s.pop()

    return revStr


if __name__ == '__main__':
    str1 = "버피는 천사다."
    print(str1)
    print(reverse_string_with_stack(str1))
