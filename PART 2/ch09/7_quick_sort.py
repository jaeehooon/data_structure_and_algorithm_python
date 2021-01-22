# 9.3 로그 선형 정렬
# 9.3.3 퀵 정렬
# 피벗(pivot) 값을 잘 선택하는 것이 성능의 핵심.
# 리스트에서 기준이 되는 하나의 요소를 피벗이라고 함
# 최선의 경우는 두 개의 n/2 크기 리스트를 생성하게 되고, 이 최선의 경우와 평균 시간복잡도는 O(n log n)임. 안정적이지 않음
# 최악의 경우 시간복잡도는 O(n^2)


def quick_sort_cache(seq):
    """
    1) 한 함수로 구현(캐시 사용)
    """
    if len(seq) < 2:
        return seq
    ipivot = len(seq) // 2      # 피벗 인덱스
    pivot = seq[ipivot]         # 피벗

    before = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    after = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    return quick_sort_cache(before) + [pivot] + quick_sort_cache(after)


def partition_devided(seq):
    """
    2) 1)의 퀵 정렬을 두 함수로 나누어 구현한다.(캐시 사용)
    """
    pivot, seq = seq[0], seq[1:]
    before = []
    after = []

    before = [x for x in seq if x <= pivot]
    after = [x for x in seq if x > pivot]
    return before, pivot, after


def quick_sort_cache_diveded(seq):
    if len(seq) < 2:
        return seq
    before, pivot, after = partition_devided(seq)
    return quick_sort_cache_diveded(before) + [pivot] + quick_sort_cache_diveded(after)


