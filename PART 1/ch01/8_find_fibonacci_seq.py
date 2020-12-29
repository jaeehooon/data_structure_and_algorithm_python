# 1.7.4 피보나치 수열
import math


def find_fibonacci_seq_iter(n):
    """
    반복문을 사용하여 피보나치 수열을 구함
    시간복잡도는 O(n)

    :param n:       몇 번째 숫자를 구하는지
    :return:        n번째의 피보나치 수열의 값
    """
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def find_fibonacci_seq_rec(n):
    """
    재귀함수를 이용하여 피보나치 수열을 구하는 메소드
    시간복잡도는 O(2^n)

    :param n:       몇 번째 숫자를 구하는지
    :return:        n번째의 피보나치 수열의 값
    """
    if n < 2:
        return n
    return find_fibonacci_seq_rec(n - 1) + find_fibonacci_seq_rec(n - 2)


def find_fibonacci_seq_form(n):
    """
    수식을 이용하여 피보나치 수열을 구하는 메소드
    시간복잡도는 O(1)

    :param n:       몇 번째 숫자를 구하는지
    :return:        n번째의 피보나치 수열의 값
    """
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** n / sq5))


def test_find_fib():
    n = 10
    assert (find_fibonacci_seq_rec(n) == 55)
    assert (find_fibonacci_seq_iter(n) == 55)
    assert (find_fibonacci_seq_form(n) == 55)
    print("test_find_fib 테스트 통과!")


if __name__ == '__main__':
    test_find_fib()
