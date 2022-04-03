from heapq import heappush, heappop


class Heap:
    def __init__(self):
        self.container = []

    def is_not_empty(self):
        return len(self.container) > 0

    def size(self):
        return len(self.container)


class Min_Heap(Heap):
    def push(self, item):
        heappush(self.container, item)

    def pop(self):
        return heappop(self.container)

    def __repr__(self):
        return str(self.container)

    def top(self):
        return self.container[0]


class Max_Heap(Heap):
    def push(self, item):
        heappush(self.container, -item)

    def pop(self):
        return -heappop(self.container)

    def __repr__(self):
        return str([-x for x in self.container])

    def top(self):
        return -self.container[0]


def test_min_heap(data=[1, 3, 5, 7, 9, 2, 4, 6, 8, 0]):

    min_heap = Min_Heap()
    for item in data:
        min_heap.push(item)
    print('min heap container: ')
    print(min_heap)

    ordered = []
    while min_heap.is_not_empty():
        ordered.append(min_heap.pop())
    print('popping elements until empty:')
    print(ordered)


def test_max_heap(data=[1, 3, 5, 7, 9, 2, 4, 6, 8, 0]):

    max_heap = Max_Heap()
    for item in data:
        max_heap.push(item)
    print('max heap container: ')
    print(max_heap)

    ordered = []
    while max_heap.is_not_empty():
        ordered.append(max_heap.pop())
    print('popping elements until empty:')
    print(ordered)


if __name__ == '__main__':

    test_min_heap()
    test_max_heap()
