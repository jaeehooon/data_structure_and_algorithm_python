# 7.7 연습문제
# 7.7.2 큐 - 데크와 회문
import string
from collections import deque
from deque_ import Deque


STRIP = string.whitespace + string.punctuation + "\"'"              #
"""
1. whitespace
    공백!

2. 구두점을 간단하게 삭제하기
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


큰 따옴표는 없음!

3. 그래서 추가로 "\"'" 해준거임
"""


def palindrome_checker_with_deque(str1):
    d1 = Deque()
    d2 = deque()

    for s in str1.lower():
        if s not in STRIP:
            d2.append(s)
            d1.enqueue(s)

    eq1 = True
    while d1.size() > 1 and eq1:
        if d1.dequeue_front() != d1.dequeue():
            eq1 = False

    eq2 = True
    while len(d2) > 1 and eq2:
        if d2.pop() != d2.popleft():
            eq2 = False

    return eq1, eq2


if __name__ == '__main__':
    str1 = "Madam Im Adam"
    str2 = "Buffy is a Slayer"

    print(palindrome_checker_with_deque(str1))
    print(palindrome_checker_with_deque(str2))
