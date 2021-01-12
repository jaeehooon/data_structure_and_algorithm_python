# 7.7 연습문제
# 7.7.1 스택 - 스택에서 최솟값 O(1)로 조회하기
# 모두 조회할 필요없이 최소값을 미리 필드에 지정해두고,
# 값을 push할때마다 최솟값을 갱신함
from stack_ import Stack


class NodeWithMin(object):

    def __init__(self, value=None, minimum=None):
        self.value = value
        self.minimum = minimum              # 얘는 연결 리스트 의미가 아님. 단순히 최솟값이 무엇인지를 담기 위한 변수


class StackMin(Stack):

    def __init__(self):
        self.items = []
        self.minimum = None

    def push(self, value):
        if self.isEmpty() or self.minimum > value:          # 스택이 비어있거나 현재 최솟값이 value값보다 크다면
            self.minimum = value                            # 새로운 값이 최솟값이 됨
        self.items.append(NodeWithMin(value, self.minimum)) # 계속 push 할 수록 self.minimum에는 self.items의 내림차순으로 저장됨

    def peek(self):
        return self.items[-1].value

    def peekMinimum(self):
        return self.items[-1].minimum

    def pop(self):
        item = self.items.pop()             # 리스트의 마지막 Node를 추출
        if item:
            if item.value == self.minimum:          # 값과 최솟값이 같다면
                self.minimum = self.peekMinimum()   # 최솟값은 위의 item을 제외한 다음 peek값
            return item.value
        else:
            print("Stack is Empty!")

    def __repr__(self):
        aux = []
        for i in self.items:
            aux.append(i.value)
        return repr(aux)


if __name__ == '__main__':
    stack = StackMin()
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print("스택에 숫자 10 ~ 1과 1 ~ 4를 추가합니다.")
    for i in range(10, 0, -1):
        stack.push(i)
    for i in range(1, 5):
        stack.push(i)
    print(stack)

    print("스택 크기: {0}".format(stack.size()))
    print("peek: {0}".format(stack.peek()))
    print("peekMinimum: {0}".format(stack.peekMinimum()))
    print("pop: {0}".format(stack.pop()))
    print("peek: {0}".format(stack.peek()))
    print("peekMinimum: {0}".format(stack.peekMinimum()))
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print(stack)
