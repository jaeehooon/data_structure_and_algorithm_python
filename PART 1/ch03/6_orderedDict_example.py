from collections import OrderedDict
"""
키 값을 변경해도 순서는 변경되지 않는다.

항목을 맨 끝으로 저장하려면, 해당 항목을 삭제한 후 다시 삽입해야함

또는 popitem() 메소드를 호출하여 딕셔너리의 마지막 키-값 항목을 제거한 후 반환될 수 있음

일반적으로, 정렬된 딕셔너리를 사용하는 것은 딕셔너리의 여러 번 순회할 것으로 예상되는 경우와
항목의 삽입을 거의 수행하지 않을 것으로 예상되는 경우에만 효율적임!
"""

def orderedDict_example():
    pairs = [("c", 1), ("b", 2), ("a", 3)]

    # 일반 딕셔너리
    d1 = {}
    for key, value in pairs:
        if key not in d1:
            d1[key] = []
        d1[key].append(value)

    for key in d1:
        print(key, d1[key])

    # OrderedDict
    d2 = OrderedDict(pairs)
    for key in d2:
        print(key, d2[key])


if __name__ == '__main__':
    orderedDict_example()
