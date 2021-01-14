# 7.7 연습문제
# 7.7.3 우선순위 큐와 힙
import heapq


def merge_sorted_seq(seq1, seq2):
    result = []
    for c in heapq.merge(seq1, seq2):
        result.append(c)
    return result


def test_merge_sorted_seq():
    seq1 = [1, 2, 3, 8, 9, 10]
    seq2 = [2, 3, 4, 5, 6, 7, 9]
    seq3 = seq1 + seq2
    assert(merge_sorted_seq(seq1, seq2) == sorted(seq3))

    print("테스트 통과!")


if __name__ == '__main__':
    test_merge_sorted_seq()
