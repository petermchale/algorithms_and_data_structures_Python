class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '(' + str(self.data) + ',' + str(self.next) + ')'


class LinkedList:

    # def __init__(self, data):
    #     self.head = Node(data)

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def __repr__(self):
        return str(self.head)


def test_linked_list():

    linked_list = LinkedList()

    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    print 'after appending:'
    print linked_list
    print

    linked_list.prepend(1)
    print 'after pre-pending:'
    print linked_list
    print

    linked_list.delete(4)
    print 'after deleting:'
    print linked_list
    print


if __name__ == '__main__':
    test_linked_list()