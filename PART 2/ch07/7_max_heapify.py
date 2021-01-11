# 7.4.3 최대 힙 구하기
class Heapify(object):
    def __init__(self, data=None):
        self.data = data or []
        for i in range(len(data)//2, -1, -1):
            self.__max_heapify__(i)

    def __repr__(self):
        return repr(self.data)

    def parent(self, i):
        if i & 1:               #  짝수 번째 인덱스임을 비교!
            return i >> 1
        else:
            return (i >> 1) - 1

    def left_child(self, i):
        return (i << 1) + 1

    def right_child(self, i):
        return (i << 1) + 2

    def __max_heapify__(self, i):
        largest = i         # 현재 노드
        left = self.left_child(i)               # 현재 노드의 왼쪽 자식 인덱스
        right = self.right_child(i)             # 현재 노드의 오른쪽 자식 인덱스
        n = len(self.data)

        # 왼쪽 자식
        # 현재 노드와 현재 노드의 왼쪽 자식을 비교!
        # 둘 중 더 큰 값이 largest에 들어감
        # 애초에 자식이 없다면 현재노드가 largest에 들어감
        largest = ((left < n and self.data[left] > self.data[i]) and left) or i

        # 오른쪽 자식
        # 현재 노드와 현재 노드의 오른쪽 자식을 비교!
        # 둘 중 더 큰 값이 largest에 들어감
        # 애초에 자식이 없다면 현재노드가 largest에 들어감
        largest = ((right < n and self.data[right] > self.data[largest]) and right) or largest

        # 현재 노드가 자식들보다 크다면 Skip, 자식이 크다면 Swap
        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]         # 현재 노드와 자식 노드의 위치 변경

            # print(self.data)
            self.__max_heapify__(largest)       # 다시 max_heapify 진행

    def extract_max(self):
        n = len(self.data)
        max_element = self.data[0]

        # 첫 번째 노드에 마지막 노드를 삽입
        self.data[0] = self.data[n - 1]
        self.data = self.data[:n - 1]
        self.__max_heapify__(0)
        return max_element

    def insert(self, item):
        i = len(self.data)
        self.data.append(item)          # 일단 item 리스트에 추가
        while (i != 0) and item > self.data[self.parent(i)]:            # 인덱스가 0이 아니고, 입력하는 값이 부모노드보다 크다면 계속 루프를 돈다.
            print(self.data)
            self.data[i] = self.data[self.parent(i)]            # 부모 노드와 현재 노드의 위치 변경
            i = self.parent(i)                  # 부모 노드의 인덱스로 변경
        self.data[i] = item                     # 부모 노드 자리에 item으로 함


def test_heapify():
    l1 = [3, 2, 5, 1, 7, 8, 2]
    h = Heapify(l1)
    assert(h.extract_max() == 8)
    print("테스트 통과!")
    h.insert(5)
    print(h)
    print("------------\n\n")
    h.insert(10)
    print(h)
    print("------------\n\n")
    h.insert(18)
    print(h)



if __name__ == '__main__':
    test_heapify()
