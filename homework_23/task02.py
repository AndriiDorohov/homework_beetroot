# Реалізувати in (__contains__) та len (__len__) методи для HashTable


class HashTable:
    def __init__(self, size=15):
        self.size = size
        self.slot = [None] * size
        self.data = [None] * size

    def hash_function(self, key):
        return key % self.size

    def re_hash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, data):
        hash_value = self.hash_function(key)  # index of data list

        if self.slot[hash_value] is None:
            self.slot[hash_value] = key
            self.data[hash_value] = data
        elif self.slot[hash_value] == key:
            self.data[hash_value] = data
        else:
            new_hash_value = self.re_hash(hash_value)
            while (
                self.slot[new_hash_value] is not None
                and self.slot[new_hash_value] != key
            ):
                new_hash_value = self.re_hash(new_hash_value)

            if self.slot[new_hash_value] is None:
                self.slot[new_hash_value] = key
                self.data[new_hash_value] = data
            else:
                self.data[new_hash_value] = data

    def get(self, key):
        start_position = self.hash_function(key)

        data = None
        found = False
        stop = False
        position = start_position
        while self.slot[position] is not None and not found and not stop:
            if self.slot[position] == key:
                data = self.data[position]
                found = True
            else:
                position = self.re_hash(position)
                if position == start_position:
                    stop = True

        return data

    def __len__(self):
        count = 0
        for key in self.slot:
            if key is not None:
                count += 1
        return count

    def __contains__(self, item):
        return item in self.slot

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __str__(self):
        representation = ""
        for key, data in zip(self.slot, self.data):
            representation += f"{key} | {data} \n"
        return representation


if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    H[88] = "frog"
    H[48] = "alien"
    print(H)

    print(H[20])

    print(H[17])
    H[20] = "duck"
    print(H[20])
    print(H[99])

    print("------------")
    print(H)
    print(len(H))
    print(21 in H)
