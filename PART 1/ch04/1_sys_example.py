# 4.1.6 sys 모듈
import sys


def main():
    for arg in sys.argv[1:]:            # sys.argv 변수는 명령줄에 전달된 인수를 프로그램 내에서 사용!
        print(arg)


if __name__ == '__main__':
    main()
