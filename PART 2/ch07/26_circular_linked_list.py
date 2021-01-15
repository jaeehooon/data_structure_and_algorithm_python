# 7.7 연습문제
# 7.7.4 연결 리스트 - 원형 연결 리스트 찾기
from linkedlist_FIFO import LinkedListFIFO
from node_ import Node


class CircularLinkedListFIFO(LinkedListFIFO):

    def _add(self, value):
        self.length += 1
        node = Node(value, self.head)               # 새로 생기는 노드의 pointer는 무조건 head가 가리키는 값으로
        if self.tail:                               # tail이 None이 아니면
            self.tail.pointer = node                # tail.pointer는 새로 생긴 node를 가리킴
        self.tail = node                            # tail은 node를 가리킴


def isCircularll(ll):
    p1 = ll.head
    p2 = ll.head
    while p2:
        try:
            p1 = p1.pointer
            p2 = p2.pointer.pointer             # 2칸씩 건너감
            # print(p1.value)
            # print(p2.value)
            # print("\n\n")
        except:
            break

        if p1 == p2:
            return True

    return False


def test_isCircularll():
    ll = LinkedListFIFO()
    for i in range(10):
        ll.addNode(i)
    assert (isCircularll(ll) is False)

    lcirc = CircularLinkedListFIFO()
    for i in range(10):
        lcirc.addNode(i)

    assert (isCircularll(lcirc) is True)

    print("테스트 통과!")


if __name__ == '__main__':
    test_isCircularll()
