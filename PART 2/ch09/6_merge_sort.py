# 9.3 로그 선형 정렬
# 9.3.2 병합 정렬
"""
    병합 정렬을 구현하는 여러 가지 방법
        --> 시간복잡도: 최악/최선/평균일 때 모두 O(n log n)
        --> 공간복잡도: 배열의 경우 O(n)이며, 일반적으로 제자리 정렬(in-place)이 아니다.
        --> 배열이 큰 경우 효율적이다.
        --> 병합 정렬의 병합 함수를 사용하여, 두 배열을 병합한다.
        --> 두 파일인 경우에도 병합 가능하다.

        가) pop() 메소드를 사용하여 다음과 같이 구현 가능.
        (각 두 배열은 정렬되어 있다.)
        def merge(left, right):
            if not left or not right:
                return left or right            # 아무것도 병합하지 않는다.
            result = []
            while left and right:
                if left[-1] >= right[-1]:
                    result.append(left.pop())
                else:
                    result.append(right.pop())
            result.reverse()
            return (left or right) + result

            >> l1 = [1, 2, 3, 4, 5, 6, 7]
            >> l2 = [2, 4, 5, 8]
            >> merge(l1, l2)
            [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]

        나) 제자리 정렬을 구현하는 경우, 한 배열의 끝에 0이 채워져 있고,
            다른 배열에는 첫 배열에서 끝에 0이 채워진 크기만큼의 요소가 있다.(각 두 배열은 정렬되어 있다.)
            >> l1 = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0]
            >> l2 = [2, 4, 5, 8]
            >> merge_two_arrays_inplace(l1, l2)
            [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]

        다) 정렬된 파일은 다음과 같이 병합(파일을 로딩할 충분한 RAM이 필요).
            >> list_files = ["1.data", "2.data", "3.data"]
            >> merge_files(list_files)
            [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
"""


def merge_sort(seq):
    """
    1) pop()을 이용한 병합 정렬
    """
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())

    res.reverse()
    return (left or right) + res


def merge_sort_sep(seq):
    """
    2) 두 함수로 나누어서 구현한다. 한 함수에서는 배열을 나누고,
        또 다른 함수에서는 배열을 병합한다.
    """
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left = merge_sort_sep(seq[:mid])
    right = merge_sort_sep(seq[mid:])
    return merge(left, right)


def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend((right[j:]))
    # print(result)
    return result


def merge_2n(left, right):
    """
    3) 각 두 배열은 정렬된 상태다.
    시간복잡도는 O(2n)이다.
    """
    if not left or not right:
        return left or right
    result = []
    while left and right:
        if left[-1] >= right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())

    result.reverse()
    return (left or right) + result


def merge_two_arrays_inplace(l1, l2):
    """
    4) 제다리 정렬로 구현한다.
    """
    if not l1 or not l2:
        return l1 or l2
    p2 = len(l2) - 1
    p1 = len(l1) - len(l2) - 1
    p12 = len(l1) - 1
    while p2 >= 0 and p1 >= 0:
        item_to_be_merged = l2[p2]
        item_bigger_array = l1[p1]
        if item_to_be_merged < item_bigger_array:
            l1[p12] = item_bigger_array
            p1 -= 1
        else:
            l1[p12] = item_to_be_merged
            p2 -= 1
        p12 -= 1
    return l1


def merge_files(list_files):
    """
    5) 파일을 병합한다.
    """
    result = []
    final = []
    for filename in list_files:
        aux = []
        with open(filename, "r") as file:
            for line in file:
                aux.append(int(line))
        result.append(aux)
    final.extend(result.pop())
    for l in result:
        final = merge(l, final)
    return final


def test_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    seq_sorted = sorted(seq)
    assert (merge_sort(seq) == seq_sorted)      # 1
    assert (merge_sort_sep(seq) == seq_sorted)  # 2

    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 = [2, 4, 5, 8]
    l_sorted = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]
    assert (merge_2n(l1, l2) == l_sorted)       # 3

    l1 = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0]
    l2 = [2, 4, 5, 8]
    l_sorted = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8]
    assert (merge_two_arrays_inplace(l1, l2) == l_sorted)       # 4

    list_files = ["a.dat", "b.dat", "c.dat"]
    l_sorted = [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
    assert (merge_files(list_files) == l_sorted)            # 5

    print("테스트 통과!")


if __name__ == '__main__':
    test_merge_sort()
