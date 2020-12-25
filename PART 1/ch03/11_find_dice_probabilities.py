# 3.4.3 주사위 경로 합계
from collections import Counter, defaultdict


def find_dice_probabilities(S, n_faces=6):
    if S > 2 * n_faces or S < 2:        # 주사위 합이 2 미만이면 None 반환
        return None

    c_dict = Counter()
    d_dict = defaultdict(list)

    # 두 주사위의 합을 모두 더해서 딕셔너리에 넣는다.
    # 그 후 합이 S인 경우를 인자로 받아 반환함
    for dice1 in range(1, n_faces+1):
        for dice2 in range(1, n_faces+1):
            t = [dice1, dice2]
            c_dict[dice1 + dice2] += 1
            d_dict[dice1 + dice2].append(t)

    return [c_dict[S], d_dict[S]]


def test_find_dice_probabilities():
    n_faces = 6
    S = 5
    results = find_dice_probabilities(S, n_faces)
    print(results)
    assert(results[0] == len(results[1]))
    print("테스트 통과!")


if __name__ == '__main__':
    test_find_dice_probabilities()
