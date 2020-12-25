# 3.4.2 애너그램
"""
애너그램은 문장 또는 단어의 철자 순서를 바꾸는 놀이를 말함

두 문자열이 서로 애너그램인지 확인하고 싶을 때,
셋(Set)은 항목의 발생 횟수를 계산하지 않고, 리스트의 항목을 정렬하는 시간복잡도는 최소 O(nlog(n))

따라서, 애너그램을 확인하는데는 딕셔너리를 사용하는 것이 좋은 해결책
"""
from collections import Counter


def is_anagram(s1, s2):
    counter = Counter()

    for c in s1:
        counter[c] += 1
    for c in s2:
        counter[c] -= 1

    for i in counter.values():
        if i:
            return False
    return True


def test_is_anagram():
    s1 = "marina"
    s2 = "aniram"
    assert(is_anagram(s1, s2) is True)
    s1 = "google"
    s2 = "gouglo"
    assert(is_anagram(s1, s2) is False)
    print("테스트 통과!")


if __name__ == '__main__':
    test_is_anagram()
