from linkedlist_FIFO import LinkedListFIFO


class DNode(object):
    def __init__(self, value=None, pointer=None, previous=None):
        self.value = value
        self.pointer = pointer
        self.previous = previous


class DLinkedList(LinkedListFIFO):
    def printListInverse(self):
        node = self.tail
        while node:
            print(node.value, end=" ")
            try:
                node = node.previous
            except AttributeError:
                break

        print()

    def _add(self, value):
        self.length += 1
        node = DNode(value)
        if self.tail:
            self.tail.pointer = node
            node.previous = self.tail
        self.tail = node

    def _delete(self, node):
        self.length -= 1
        node.previous.pointer = node.pointer
        if not node.pointer:
            self.tail = node.previous

    def _find(self, index):
        node = self.head
        i = 0
        while node and i < index:
            node = node.pointer
            i += 1
        return node, i

    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, i = self._find(index)
            if i == index:
                self._delete(node)
            else:
                print("인덱스 {0}에 해당하는 노드가 없습니다.".format(index))


if __name__ == '__main__':
    from collections import Counter

    ll = DLinkedList()
    for i in range(1, 5):
        ll.addNode(i)
    print("연결 리스트 출력: ")
    ll._printList()
    print('연결 리스트 반대로 출력: ')
    ll.printListInverse()
    print("값이 15인 노드 추가 후, 연결 리스트 출력: ")
    ll._add(15)
    ll._printList()
    print("모든 노드 모두 삭제 후, 연결 리스트 출력: ")
    for i in range(ll.length-1, -1, -1):
        ll.deleteNode(i)
    ll._printList()
