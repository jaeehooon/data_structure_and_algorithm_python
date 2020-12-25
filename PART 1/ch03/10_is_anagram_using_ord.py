# 3.4.2 애너그램 (2)
"""
ord() 함수는 인수가 유니코드 객체일 때, 문자의 유니코드를 나타내는 정수를 반환
인수가 8바이트 문자열인 경우 바이트 값을 반환함

문자열에서 모든 문자의 ord() 함수 결과를 더했을 때 그 결과가 같으면 두 문자열은 애너그램

"""
import string


def hash_func(astring):
    """

    :param astring:
    :return:
    """
    s = 0
    for one in astring:
        if one in string.whitespace:
            continue
        s += ord(one)
    return s


def find_anagram_hash_function(word1, word2):
    return hash_func(word1) == hash_func(word2)


def test_find_anagram_hash_function():
    word1 = "buffy"
    word2 = "bffyu"
    word3 = "bffya"
    assert(find_anagram_hash_function(word1, word2) is True)
    assert(find_anagram_hash_function(word1, word3) is False)
    print("테스트 통과!")


if __name__ == '__main__':
    test_find_anagram_hash_function()
