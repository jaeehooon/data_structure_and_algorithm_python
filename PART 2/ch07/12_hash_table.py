# 7.6 해시 테이블
from linkedlist_FIFO import LinkedListFIFO


class HashTableLL(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._createHashTable()

    def _createHashTable(self):
        for i in range(self.size):
            self.slots.append(LinkedListFIFO())

    def _find(self, item):
        return item % self.size

    def _add(self, item):
        index = self._find(item)
        self.slots[index].addNode(item)

    def _delete(self, item):
        index = self._find(item)
        self.slots[index].deleteNodeByValue(item)

    def _print(self):
        for i in range(self.size):
            print("슬롯(slot) {0}: ".format(i))
            self.slots[i]._printList()


def test_hash_tables():
    H1 = HashTableLL(3)
    for i in range(0, 20):
        H1._add(i)
    H1._print()
    print("\n항목 0, 1, 2를 삭제합니다.")
    H1._delete(0)
    H1._delete(1)
    H1._delete(2)
    H1._print()


if __name__ == '__main__':
    test_hash_tables()
