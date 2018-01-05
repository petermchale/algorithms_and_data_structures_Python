class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def peek(self):
        return self.top.data

    def push(self, data):
        node_to_add = Node(data)
        node_to_add.next = self.top
        self.top = node_to_add

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data


def test_stack():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print stack.peek()
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.is_empty()


if __name__ == "__main__":
    test_stack()


