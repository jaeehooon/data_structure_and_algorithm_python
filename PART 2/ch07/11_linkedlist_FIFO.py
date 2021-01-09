# 7.5 연결 리스트
from node_ import Node


class LinkedListFIFO(object):
    def __init__(self):
        self.head = None        # 헤드(머리)
        self.length = 0
        self.tail = None        # 테일(꼬리)

    # 헤드부터 각 노드의 값을 출력한다.
    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()

    # 첫 번째 위치에 노드를 추가한다.
    def _addFirst(self, value):
        self.length = 1
        node = Node(value)
        self.head = node
        self.tail = node

    # 첫 번쨰 위치의 노드를 삭제한다.
    def _deleteFirst(self):
        self.length = 0
        self.head = None
        self.tail = None
        print('연결 리스트가 비어있습니다.')

    # 새 노드를 추가한다. 테일이 있다면, 테일의 다음 노드는
    # 새 노드를 가리키고, 테일은 새 노드를 가리킨다.
    def _add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node
        self.tail = node

    # 새 노드를 추가한다.
    def addNode(self, value):
        if not self.head:
            self._addFirst(value)
        else:
            self._add(value)

    # 인덱스로 노드를 찾는다.
    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    # 값으로 노드를 찾는다.
    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    # 인덱스에 해당하는 노드를 삭제한다.
    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print("인덱스 {0}에 해당하는 노드가 없습니다.".format(index))

    # 값에 해당하는 노드를 삭제한다.
    def deleteNodeByValue(self, value):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, prev, i = self._find_by_value(value)
            if node and node.value == value:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print("값 {0}에 해당하는 노드가 없습니다.".format(value))


if __name__ == '__main__':
    ll = LinkedListFIFO()
    for i in range(1, 5):
        ll.addNode(i)
    print('연결 리스트 출력: ')
    ll._printList()
    print("인덱스가 2인 노드 삭제 후, 연결 리스트 출력: ")
    ll.deleteNode(2)
    ll._printList()
    print("값이 15인 노드 추가 후, 연결 리스트 출력: ")
    ll.addNode(15)
    ll._printList()
    print("모두 노드 모두 삭제 후, 연결 리스트 출력: ")
    for i in range(ll.length-1, -1, -1):
        ll.deleteNode(i)
    ll._printList()
