# 3-4. [3] Design a dictionary data structure in which search, insertion, and deletion can
#   all be processed in O(1) time in the worst case. You may assume the set elements
#   are integers drawn from a finite set 1, 2, .., n, and initialization can take O(n) time.

from abc import ABC, abstractmethod
from shutil import Error

DELETED = object()  # Unique marker for deleted entries

class HashTable(ABC):
    @staticmethod
    def create(collision_res: str = "open_addressing", **kwargs):
        if collision_res == "open_addressing":
            return _OpenAddressingHashTable(**kwargs)
        # elif collision_res == "chaining":
        #     return _ChainingHashTable(**kwargs)

    def __init__(self, init_capacity: int, hash_function: str):
        self.capacity = init_capacity
        self.hash_function = hash_function
        self.size = 0
        self.table = [None] * init_capacity

    def _hash(self, value) -> int:
        key = -1
        if isinstance(value, str):
            p = 37
            key = sum(ord(char) * p ** i for i, char in enumerate(value)) % self.capacity
        elif isinstance(value, float):
            p = 10 ** len(str(value).split(".")[1])
            key = (int(value * p)) % self.capacity
        elif isinstance(value, int):
            key = value % self.capacity
        return key

    @abstractmethod
    def insert(self, value) -> bool:
        pass

    @abstractmethod
    def find(self, value):
        pass

    @abstractmethod
    def delete(self, value):
        pass


class _OpenAddressingHashTable(HashTable, ABC):
    def __init__(self, init_capacity: int = 31, hash_function: str = "division", load_factor: float = 0.7,
                 probing: str = "linear"):

        if load_factor > 0.9:
            raise Error("Can't initialize with load factor greater than 0.9")

        super().__init__(init_capacity, hash_function)
        self.probing = probing
        self.load_factor = load_factor

    def _grow(self):
        self.capacity *= 2
        new_table = [None] * self.capacity

        for i, x in enumerate(self.table):
            new_table[i] = x

        self.table = new_table
        return

    def insert(self, value) -> bool:
        if self.size + 1 >= self.load_factor * self.capacity:
            self._grow()

        key = self._hash(value)

        while True:
            if self.table[key] is None or self.table[key] == DELETED or self.table[key] == value:
                break

            if key + 1 == self.capacity:
                key = 0
            else:
                key += 1

        if self.table[key] is None or self.table[key] == DELETED:
            self.table[key] = value
            self.size += 1
            return True
        else:
            raise ValueError("Value already exists in table")

    def find(self, value) -> int:
        key = self._hash(value)

        if self.table[key] is None:
            return -1
        elif self.table[key] == value:
            return key

        next_key = key + 1

        while next_key != key:
            if self.table[next_key] is None or self.table[next_key] == value:
                break

            if next_key + 1 == self.capacity:
                next_key = 0
            else:
                next_key += 1

        if next_key == key or self.table[next_key] is None:
            return -1
        else:
            return next_key

    def delete(self, value):
        key = self.find(value)

        if key == -1:
            raise ValueError("The entered value does not exist")
        else:
            self.table[key] = DELETED
            self.size -= 1

            return value


