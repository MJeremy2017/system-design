from typing import List


# The tricky part is that class variables and default arguments are created when
# the function is loaded (and only once), that means that any changes to
# a "mutable default argument" or "mutable class variable" are permanent
class Heap:
    def __init__(self, A: List[int]=None):
        if A is None:
            A = []
        self.A = A

    def heappush(self, value):
        self.A.append(value)
        index = len(self.A) - 1
        parent_index = self._get_parent_index(index)
        while parent_index >= 0 and self.A[index] < self.A[parent_index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = self._get_parent_index(index)

    def heappop(self) -> int:
        if len(self.A):
            value = self.A[0]
            self._swap(0, -1)
            self.A.pop()
            self.perc_down(0)
            return value
        raise ValueError("Empty heap")

    def perc_down(self, index):
        n = len(self.A)
        while 1:
            left, right = self._get_child_index(index)
            if left < n and right < n:
                if self.A[index] <= min(self.A[left], self.A[right]):
                    break
                if self.A[left] < self.A[right]:
                    self._swap(index, left)
                    index = left
                else:
                    self._swap(index, right)
                    index = right
                continue
            if left < n and self.A[index] > self.A[left]:
                self._swap(index, left)
                index = left
            if right < n and self.A[index] > self.A[right]:
                self._swap(index, right)
                index = right
            break

    def heapify(self):
        index = (len(self.A) >> 1) - 1
        for i in range(index, -1, -1):
            self.perc_down(i)

    def peek(self):
        if len(self.A):
            return self.A[0]
        raise ValueError("Empty heap")

    def get_heap(self):
        return self.A

    def _get_parent_index(self, index) -> int:
        return (index - 1) >> 1

    def _swap(self, i, j):
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def _get_child_index(self, index):
        return 2 * index + 1, 2 * index + 2


class TestHeap:
    def test_heappush(self):
        hq = Heap()
        hq.heappush(4)
        print(hq.get_heap())

        hq.heappush(2)
        print(hq.get_heap())

        hq.heappush(1)
        print(hq.get_heap())

    def test_heappop(self):
        hq = Heap()
        hq.heappush(12)
        hq.heappush(3)
        hq.heappush(-2)
        hq.heappush(14)
        hq.heappush(5)

        for i in range(5):
            print(hq.heappop())
        print("----------------")

    def test_heapify(self):
        A = [3, 12, 1, 6, -10, 4, 7, 15, 3, 2]
        hq = Heap(A)
        hq.heapify()
        # print("heapify", hq.get_heap())
        for i in range(len(A)):
            print(hq.heappop())
        print("----------------")


if __name__ == '__main__':
    th = TestHeap()
    th.test_heappush()
    th.test_heappop()

    th.test_heapify()
