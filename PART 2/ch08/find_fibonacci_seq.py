# 8.3 함수의 실행 시간
def find_fibonacci_seq_rec(n):
    if n < 2:
        return n
    return find_fibonacci_seq_rec(n - 1) + find_fibonacci_seq_rec(n - 2)


if __name__ == '__main__':
    print(find_fibonacci_seq_rec(5))
