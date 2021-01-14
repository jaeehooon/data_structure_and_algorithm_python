# 7.7 연습문제
# 7.7.4 연결 리스트 - 연결 리스트 분할하기
from node_ import Node
from linkedlist_FIFO import LinkedListFIFO


def partList(ll, n):
    more = LinkedListFIFO()
    less = LinkedListFIFO()

    node = ll.head

    while node:
        item = node.value

        if item < n:
            less.addNode(item)
        elif item > n:
            more.addNode(item)

        node = node.pointer

    less.addNode(n)
    node_more = more.head

    while node_more:
        less.addNode(node_more.value)
        node_more = node_more.pointer

    return less


if __name__ == '__main__':
    ll = LinkedListFIFO()
    l = [6, 7, 3, 4, 9, 5, 1, 2, 8]
    for i in l:
        ll.addNode(i)

    print("분할 전: ")
    ll._printList()

    print("분할 후: ")
    newll = partList(ll, 6)
    newll._printList()
