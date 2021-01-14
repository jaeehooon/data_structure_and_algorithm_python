# 7.7 연습문제
# 7.7.4 연결 리스트 - 끝에서 k번째 항목 찾기
from node_ import Node
from linkedlist_FIFO import LinkedListFIFO


class KthFromLast(LinkedListFIFO):

    def find_kth_to_last(self, k):
        p1, p2 = self.head, self.head
        i = 0
        while p1:
            if i > k-1:
                try:
                    p2 = p2.pointer
                except AttributeError:
                    break
            p1 = p1.pointer
            i += 1
        return p2.value


if __name__ == '__main__':
    ll = KthFromLast()
    for i in range(1, 11):
        ll.addNode(i)
    print("연결 리스트 : ", end="")
    ll._printList()
    k = 3
    k_from_last = ll.find_kth_to_last(k)
    print("연결 리스트의 끝에서 {0}번째 항목은 {1}입니다.".format(k, k_from_last))
