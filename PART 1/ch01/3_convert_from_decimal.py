# 1.7.1 진법변환
def convert_from_decimal(number, base):
    """
    10진수에서 다른 진법의 숫자로 변환하는 메소드

    :param number:  10진수 숫자
    :param base:    변환할 진법
    :return:        변환된 진법의 숫자
    """
    multiplier, result = 1, 0
    while number > 0:
        result += (number % base * multiplier)
        multiplier *= 10
        number //= base

    return result


def test_convert_from_decimal():
    number, base = 9, 2
    assert(convert_from_decimal(number, base) == 1001)
    print("test_convert_from_decimal 테스트 통과!")


if __name__ == '__main__':
    test_convert_from_decimal()
