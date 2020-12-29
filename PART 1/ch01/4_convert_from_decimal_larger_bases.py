# 1.7.1 진법 변환

def convert_from_decimal_larger_bases(number, base):
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit = number % base
        result = strings[digit] + result            # 주의!
        number //= base

    return result


def test_convert_from_decimal_larger_bases():
    number, base = 31, 16
    assert(convert_from_decimal_larger_bases(number, base) == "1F")
    print("convert_from_decimal_larger_bases 테스트 통과!")


if __name__ == '__main__':
    test_convert_from_decimal_larger_bases()
