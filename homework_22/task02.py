# Task 2

# Implement a stack using a singly linked list.

from node import Node


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def is_empty(self):
        return self._top is None

    def push(self, item):
        new_node = Node(item)
        new_node.set_next(self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        top_data = self._top.get_data()
        self._top = self._top.get_next()
        self._size -= 1
        return top_data

    def peek(self):
        if self.is_empty():
            return None
        return self._top.get_data()

    def size(self):
        return self._size

    def __repr__(self):
        representation = "<Stack>\n"
        current = self._top
        index = 1
        while current is not None:
            representation += f"{index}: {str(current.get_data())}\n"
            current = current.get_next()
            index += 1
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack()

    print(s.is_empty())
    s.push(4)
    s.push("dog")
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.pop())
    print(s)
