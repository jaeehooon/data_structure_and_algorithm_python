# 1.7.3 random 모듈
import random


def testing_random():
    """ random 모듈 테스트 """
    values = [1, 2, 3, 4]
    print(random.choice(values))        # 리스트 내의 값들 중 임의로 하나를 뽑는다.
    print(random.choice(values))
    print(random.choice(values))
    print(random.sample(values, 2))     # 리스트 내의 값들 중 임의로 값을 2개 뽑는다. (중복 X)
    print(random.sample(values, 3))     # 리스트 내의 값들 중 임의로 값을 3개 뽑는다. (중복 X)

    """ 리스트를 섞는다. """
    random.shuffle(values)
    print(values)

    """ 0~10의 임의의 정수를 생성한다. """
    print(random.randint(0, 10))        # 0~10 사이의 숫자 중 하나를 선택
    print(random.randint(0, 10))


if __name__ == '__main__':
    testing_random()
