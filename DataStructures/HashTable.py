# 3-4. [3] Design a dictionary data structure in which search, insertion, and deletion can
#   all be processed in O(1) time in the worst case. You may assume the set elements
#   are integers drawn from a finite set 1, 2, .., n, and initialization can take O(n) time.

from abc import ABC, abstractmethod


class HashTable(ABC):
    @classmethod
    def __new__(cls, collision_res: str = "chaining", init_capacity: int = 31, load_factor: float = 0.7,
                hash_function: str = "division", *args, **kwargs):

        if collision_res == "chaining":
            return _ChainingHashTable(init_capacity, load_factor, hash_function)
        if collision_res == "open_addressing":
            return _OpenAddressingHashTable(init_capacity, load_factor, hash_function)

    @abstractmethod
    def __init__(self, init_capacity=31, load_factor=0.7, hash_function="division"):
        self.capacity = init_capacity
        self.load_factor = load_factor
        self.hash_function = hash_function
        self.size = 0
        self.table = [None]*init_capacity

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.nxt = None

    @abstractmethod
    def _hash(self, key) -> int:
        key_hash = -1
        # If key is String:
        # Polynomial Rolling Hash: Treat the string as a polynomial and compute
        # an integer value using a constant p, e.g., hash_value = sum(ord(char) * p ** i
        # for i, char in enumerate(string))
        if isinstance(key, str):
            p = 37
            key_hash = sum(ord(char) * p **i for i, char in enumerate(key)) % self.capacity

        # If key is Float
        # A simple approach is to multiply the float by a large power of 10 to remove decimal precision,
        # converting it to an integer.This works well for hashing as it makes slight changes in the
        # float representation produce unique hash values.Example: int(float_val * 10000)
        elif isinstance(key, float):
            key_str = str(key)
            decimal_places = len(key_str.split(".")[1])
            p = 10 ** decimal_places
            key_hash = (key * p) % self.capacity

        # If key is Integer
        elif isinstance(key, int):
            key_hash = key % self.capacity

        return key_hash

    @abstractmethod
    def insert(self, key, value) -> bool:
        pass

    @abstractmethod
    def find(self, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass


class _ChainingHashTable(HashTable):
    def __init__(self, init_capacity, load_factor, hash_function):
        super().__init__(init_capacity, load_factor, hash_function)


class _OpenAddressingHashTable(HashTable):
    def __init__(self, init_capacity, load_factor, hash_function):
        super().__init__(init_capacity, load_factor, hash_function)

    def _grow(self):
        self.capacity *= 2
        new_table = [None] * self.capacity

        for i, x in enumerate(self.table):
            new_table[i] = x

        self.table = new_table
        return

    def insert(self, key, value) -> bool:
        key_hash = self._hash(key)

        while self.table[key_hash] is not None:
            if self.size >= 0.7 * self.capacity:
                self._grow()

            if key_hash >= len(self.table):
                key_hash = 0
                continue

            key_hash += 1

        self.table[key_hash] = value
        return True
