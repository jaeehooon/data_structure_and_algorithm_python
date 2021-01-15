# 7.7 연습문제
# 7.7.4 연결 리스트 - 두 연결 리스트의 숫자 더하기
from linkedlist_FIFO import LinkedListFIFO
from node_ import Node


class LinkedListFIFOYield(LinkedListFIFO):

    def _printList(self):
        node = self.head
        while node:
            yield node.value
            node = node.pointer


def sumlls(l1, l2):
    lsum = LinkedListFIFOYield()
    dig1 = l1.head
    dig2 = l2.head
    pointer = 0                     # 각 자릿수를 더헀을 때 10을 넘어가면 올림 수. 즉 1

    while dig1 and dig2:
        d1 = dig1.value
        d2 = dig2.value
        sum_d = d1 + d2 + pointer

        if sum_d > 9:
            pointer = sum_d // 10
            lsum.addNode(sum_d % 10)
        else:
            lsum.addNode(sum_d)
            pointer = 0
        dig1 = dig1.pointer
        dig2 = dig2.pointer

    # 아래는 더하는 두 숫자의 자릿수가 맞지 않을 때
    if dig1:
        sum_d = pointer + dig1.value
        if sum_d > 9:
            lsum.addNode(sum_d % 10)
        else:
            lsum.addNode(sum_d)
        dig1 = dig1.pointer             # 없어도 될 것 같지만 dig1을 None으로 하기 위한 조치

    if dig2:
        sum_d = pointer + dig2.value
        if sum_d > 9:
            lsum.addNode(sum_d % 10)
        else:
            lsum.addNode(sum_d)
        dig2 = dig2.pointer         # 없어도 될 것 같지만 dig2을 None으로 하기 위한 조치

    return lsum


if __name__ == '__main__':
    l1 = LinkedListFIFOYield()      # 2671
    l1.addNode(1)
    l1.addNode(7)
    l1.addNode(6)
    l1.addNode(2)

    l2 = LinkedListFIFOYield()      # 455
    l2.addNode(5)
    l2.addNode(5)
    l2.addNode(4)

    lsum = sumlls(l1, l2)
    l = list(lsum._printList())     # [6, 2, 1, 3]
    for i in reversed(l):
        print(i, end="")
    print()
