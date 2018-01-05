class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def peek(self):
        return self.head.data

    def add(self, data):
        node_to_add = Node(data)
        if self.tail is not None:
            self.tail.next = node_to_add
        self.tail = node_to_add
        if self.head is None:
            self.head = node_to_add

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data


def test_queue():
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    print queue.peek()
    print queue.remove()
    print queue.remove()
    print queue.remove()
    print queue.is_empty()


if __name__ == "__main__":
    test_queue()
