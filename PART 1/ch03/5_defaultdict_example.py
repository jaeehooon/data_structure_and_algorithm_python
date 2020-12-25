# 3.3.1 기본 딕셔너리

from collections import defaultdict


def defaultdict_example():
    pairs = {("a", 1), ("b", 2), ("c", 3)}

    # 일반 딕셔너리
    d1 = {}
    for key, value in pairs:
        if key not in d1:
            d1[key] = []
        d1[key].append(value)
    print(d1)

    # defaultdict
    d2 = defaultdict(list)
    for key, value in pairs:
        d2[key].append(value)
    print(d2)


if __name__ == '__main__':
    defaultdict_example()
