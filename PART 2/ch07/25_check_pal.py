# 7.7 연습문제
# 7.7.4 연결 리스트 - 회문 확인하기
from linkedlist_FIFO import LinkedListFIFO
from node_ import Node


def isPal(l1):
    if len(l1) < 2:
        return True
    if l1[0] != l1[-1]:
        return False
    return isPal(l1[1:-1])


def checkllPal(ll):
    node = ll.head
    l = []

    while node is not None:
        l.append(node.value)
        node = node.pointer

    return isPal(l)


def test_checkllPal():
    ll = LinkedListFIFO()
    l1 = [1, 2, 3, 2, 1]
    for i in l1:
        ll.addNode(i)
    assert (checkllPal(ll) is True)

    ll.addNode(2)
    ll.addNode(3)
    assert (checkllPal(ll) is False)

    print("테스트 통과!")


if __name__ == '__main__':
    test_checkllPal()
