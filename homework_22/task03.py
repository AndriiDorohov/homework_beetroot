# Task 3

# Implement a queue using a singly linked list.
from node import Node


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.set_next(new_node)
            self._tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        item = self._head.get_data()
        self._head = self._head.get_next()
        if self._head is None:
            self._tail = None
        return item

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def __repr__(self):
        representation = "<Queue>\n"
        current = self._head
        while current is not None:
            representation += f"{str(current.get_data())}\n"
            current = current.get_next()
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue("dog")
    q.enqueue(True)
    print(q.size())
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
