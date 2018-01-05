# https://www.youtube.com/watch?v=7ArHz8jPglw&index=31&list=PLOuZYwbmgZWXvkghUyMLdI90IwxbNCiWK

from stack import Stack


class Queue:
    def __init__(self):
        self.stack_newest_on_top = Stack()
        self.stack_oldest_on_top = Stack()

    def shift_stacks(self):
        if self.stack_oldest_on_top.is_empty():
            while self.stack_newest_on_top.is_empty() is False:
                self.stack_oldest_on_top.push(self.stack_newest_on_top.pop())

    def peek(self):
        self.shift_stacks()
        return self.stack_oldest_on_top.peek()

    def enqueue(self, data):
        self.stack_newest_on_top.push(data)

    def dequeue(self):
        self.shift_stacks()
        return self.stack_oldest_on_top.pop()


def test_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print queue.peek()
    print queue.dequeue()
    print queue.dequeue()
    print queue.dequeue()


if __name__ == "__main__":
    test_queue()
