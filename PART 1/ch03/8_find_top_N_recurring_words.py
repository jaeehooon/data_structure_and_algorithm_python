# 3.4.1 단어 횟수 세기
from collections import Counter


def find_top_N_recurring_words(seq, N):
    """
    문자열에서 가장 많이 나오는 단어와 횟수를 반환하는 메소드

    :param seq:     입력으로 받는 문자열
    :param N:       가장 많이 나오는 단어의 갯수
    :return:        가장 많이 나오는 단어와 그 횟수를 튜플로, 전체적으로 리스트로서 반환함
    """
    d_counter = Counter()
    for word in seq.split():
        d_counter[word] += 1
    return d_counter.most_common(N)


def test_find_top_N_recurring_words():
    seq = "버피 에인절 몬스터 잰더 윌로 버피 몬스터 슈퍼 버피 에인절"
    N = 3
    assert(find_top_N_recurring_words(seq, N) == [("버피", 3), ("에인절", 2), ("몬스터", 2)])
    print("테스트 통과!")


if __name__ == '__main__':
    test_find_top_N_recurring_words()
