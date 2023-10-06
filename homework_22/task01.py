# Task 1

# Extend UnorderedList

# Implement append, index, pop, insert methods for UnorderedList.
# Also implement a slice method, which will take two parameters
# 'start' and 'stop', and return a copy of the list starting at
# the position and going up to but not including the stop position.


from node import Node


class OrderedList:
    def __init__(self):
        self._head = None

    def search(self, item):
        current = self._head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def index(self, item):
        current = self._head
        found = False
        found_index = 0
        while current != None and not found:
            found_index += 1
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found_index - 1

    def add(self, item):
        current = self._head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self._head)
            self._head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def pop(self):
        current = self._head
        result = None
        done = False
        previous = None
        while not done:
            if current.get_next() is None:
                result = current.get_data()
                if previous is None:
                    self._head = None
                else:
                    previous.set_next(None)
                return result
            else:
                previous = current
                current = current.get_next()

    def slice(self, start, stop):
        current = self._head
        finish = False
        count = 0
        my_list = []
        while not finish:
            if count >= start and count <= stop:
                my_list.append(current.get_data())
            if count - 1 == stop:
                finish = True
            else:
                current = current.get_next()
            count += 1
        return my_list

    def is_empty(self):
        return self._head is None

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = OrderedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    my_list.remove(54)

    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))
    print(my_list.pop())
    print(my_list.size())
    print(my_list.index(77))
    print(my_list)
    print(my_list.slice(1, 3))
