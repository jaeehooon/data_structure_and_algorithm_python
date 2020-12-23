# 3.2.2 딕셔너리 성능 측정
"""
멤버십 연산에 대한 시간복잡도
리스트 : O(n)
딕셔너리 : O(1)

"""
import timeit
import random


for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")

    x = list(range(i))      # 리스트
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}     # 딕셔너리
    d_time = t.timeit(number=1000)
    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))


