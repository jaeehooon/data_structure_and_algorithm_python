# 7.3 데크
from queue_ import Queue


class Deque(Queue):
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        value = self.items.pop(0)
        if value is not None:
            return value
        else:
            print("Deque is empty!")


if __name__ == '__main__':
    deque = Deque()
    print("데크(Deque)가 비었나요? {0}".format(deque.isEmpty()))
    print("데크에 숫자 0~9를 추가합니다.")
    for i in range(10):
        deque.enqueue(i)
    print("데크 크기: {0}".format(deque.size()))
    print("peek: {0}".format(deque.peek()))
    print("dequeue: {0}".format(deque.dequeue()))
    print("peek: {0}".format(deque.peek()))
    print("데크가 비었나요? {0}".format(deque.isEmpty()))
    print()
    print("데크: {0}".format(deque))
    print("dequeue: {0}".format(deque.dequeue_front()))
    print("peek: {0}".format(deque.peek()))
    print("데크: {0}".format(deque))
    print("enqueue_back(50)을 수행합니다.")
    deque.enqueue_back(50)
    print("peek: {0}".format(deque.peek()))
    print("데크: {0}".format(deque))
