# 7.7 연습문제
# 7.7.1 스택 - 스택 집합
from stack_ import Stack


class SetOfStacks(Stack):

    def __init__(self, capacity=4):
        self.set_of_stacks = []         # 여러 개의 스택(리스트)들을 담는 리스트. self.items가 다 차면 그 스택을 본 변수에 담음
        self.items = []
        self.capacity = capacity

    def push(self, value):
        if self.size() >= self.capacity:
            self.set_of_stacks.append(self.items)
            self.items = []

        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if self.isEmpty() and self.set_of_stacks:           # 현재 스택(self.items)가 비어있고 아직 스택 집합의 스택이 존재하면
            self.items = self.set_of_stacks.pop()           # 현재 스택(self.items)에 담을 스택을 전체 스택 집합으로 부터 pop함
        return value

    def sizeStack(self):
        return len(self.set_of_stacks) * self.capacity + self.size()

    def __repr__(self):
        aux = []
        for s in self.set_of_stacks:
            aux.extend(s)               # 리스트의 뒤쪽으로 추가함
        aux.extend(self.items)
        return repr(aux)


if __name__ == '__main__':
    capacity = 5
    stack = SetOfStacks(capacity)
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print("스택에 숫자 0 ~ 9를 추가합니다.")
    for i in range(30):
        stack.push(i)

    print()
    print("스택 크기:\t{0}".format(stack.sizeStack()))
    print("peek:\t{0}".format(stack.peek()))
    print("pop:\t{0}".format(stack.pop()))
    print("peek:\t{0}".format(stack.peek()))
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print(stack)
