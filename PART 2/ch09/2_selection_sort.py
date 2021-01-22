# 9.1 2차 정렬
# 9.1.2 선택 정렬
# O(n^2), 안정적이지 않음
def selection_sort(seq):
    length = len(seq)
    for i in range(length-1):
        min_j = i
        for j in range(i+1, length):                # 최솟값을 찾는 과정
            if seq[min_j] > seq[j]:                 # 최솟값을 찾으면
                min_j = j
        seq[i], seq[min_j] = seq[min_j], seq[i]     # i번째 위치와 최솟값 위치를 바꿈

    return seq


def test_selection_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert(selection_sort(seq) == sorted(seq))
    print("테스트 통과!")


if __name__ == '__main__':
    test_selection_sort()
