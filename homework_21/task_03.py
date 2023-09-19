# #!/usr/bin/env python3

# Task 3

# Extend the Stack to include a method called get_from_stack
# that searches and returns an element e from a stack.
# Any other element must remain on the stack respecting their order.
# Consider the case in which the element is not found
# - raise ValueError with proper info Message

class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

    def get_from_stack(self, item):
        if item in self._items:
            index = self._items.index(item)
            return self._items.pop(index)
        else:
            raise ValueError(f"{item} not found")

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def size(self):
        return len(self._items)

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        return self._items.pop(0)

    def front(self):
        if self._items:
            return self._items[0]
        else:
            return None

    def rear(self):
        try:
            return self._items[-1]
        except IndexError:
            return None

    def get_from_queue(self, item):
        if item in self._items:
            index = self._items.index(item)
            return self._items.pop(index)
        else:
            raise ValueError(f"{item} not found")

    def __repr__(self):
        # return f'<Queue> => {" ".join([str(item) for item in self._items])}'
        representation = "<Queue>\n"
        for ind, item in enumerate(self._items, 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def __contains__(self, item):
        return item in self._items


if __name__ == "__main__":
    s = Stack()
    s.push("a")
    s.push("r")
    s.push("cс")
    print(s.get_from_stack("cс"))
    print(s)

    q = Queue()
    q.enqueue("t")
    q.enqueue("w")
    q.enqueue("zzz")
    print(q.get_from_queue("z"))
    print(q)
