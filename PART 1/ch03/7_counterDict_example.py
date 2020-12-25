from collections import Counter
"""
Counter 는 해시 가능한(hashable) 객체를 카운팅하는 서브 클래스

Counter 를 사용한 결과는 카운트가 많이 된 순서대로 출력됨
"""


def counter_example():
    """ 항목의 발생 횟수를 매핑하는 딕셔너리를 생성한다. """
    seq1 = [1, 2, 3, 5, 1, 2, 5, 5, 2, 5, 1, 4]
    seq_counts = Counter(seq1)
    print(seq_counts)

    print("\n-------------------\n")

    """ 항목의 발생 횟수를 수동으로 갱신하거나, update() 메소드를 사용할 수 있다. """
    seq2 = [1, 2, 3]
    seq_counts.update(seq2)             # update, add
    print(seq_counts)

    print("\n-------------------\n")

    seq3 = [1, 4, 3]
    for key in seq3:
        seq_counts[key] += 1
    print(seq_counts)

    print("\n-------------------\n")

    """ a+b, a-b 같은 셋 연산을 사용할 수 있다. """
    seq_counts_2 = Counter(seq3)
    print(seq_counts_2)

    print("\n-------------------\n")

    print(seq_counts + seq_counts_2)
    print(seq_counts - seq_counts_2)
    print(seq_counts & seq_counts_2)
    print(seq_counts | seq_counts_2)


if __name__ == '__main__':
    counter_example()
