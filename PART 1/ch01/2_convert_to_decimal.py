# 1.7 연습문제
# 1.7.1 진법 변환


def convert2decimal(value, base):
    """
    다르 진법의 숫자를 10진수로 변환하는 메소드
    2 <= base <= 10

    :return:    10진수로 변환된 값
    """
    return int(str(value), base)


"""
교재 코드
"""
def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier              # 1의 자리부터 시작
        multiplier *= base
        number //= 10
    return result


def test_convert_to_decimal():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)
    print("test_convert_to_decimal 테스트 통과!")


if __name__ == '__main__':
    print(convert2decimal(111, 2))
    print(convert2decimal(1001, 2))

    test_convert_to_decimal()
