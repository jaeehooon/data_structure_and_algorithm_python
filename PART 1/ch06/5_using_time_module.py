# 6.2.3 프로파일링
import time


def sumOfN2(n):
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
        theSum += i
    end = time.time()
    return theSum, end - start


if __name__ == '__main__':
    n = 5
    print("총 합계: %d\t 시간: %10.7f초" % sumOfN2(n))
    n = 200
    print("총 합계: %d\t 시간: %10.7f초" % sumOfN2(n))
