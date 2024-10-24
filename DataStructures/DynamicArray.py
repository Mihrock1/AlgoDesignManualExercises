from binascii import Error
from typing import Union

class DynamicArray:
    def __init__(self, capacity: int = 0):
        # length user things the dynamic array is
        self.size = 0
        # actual length of dynamic array
        self.capacity = capacity
        self.array = [None] * capacity

    def get_size(self):
        return self.size

    def __grow(self):
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i, obj in enumerate(self.array):
            new_arr[i] = obj

        self.array = new_arr

    def add(self, obj):
        if self.size == self.capacity:
            self.__grow()

        self.array[self.size] = obj
        self.size += 1

    def add_first(self, obj):
        if self.size == self.capacity:
            self.__grow()

        new_arr = []
        new_arr[0] = obj

        for i, obj in enumerate(self.array):
            new_arr[i+1] = obj

        self.size += 1
        self.array = new_arr

    def pop(self):
        obj = self.array[self.size - 1]
        self.array[self.size - 1] = None

        self.size -= 1
        return obj

    def remove_first(self):
        obj = self.array[0]
        self.array[0] = None

        for i, x in enumerate(self.array):
            if i == 0:
                continue

            self.array[i-1] = x

        self.size -= 1
        return obj

    def remove_index(self, index):
        if index >= self.size:
            raise ValueError("Index larger than array size")

        obj = self.array[index]
        self.array[index] = None

        for i in range(index+1, len(self.array)):
            self.array[i - 1] = self.array[i]

        # for i, x in enumerate(self.array[index+1:]):
        #     self.array[i-1] = x

        self.size -= 1
        return obj

    def remove(self, obj):
        index = self.find(obj)

        if index is not None:
            self.remove_index(index)

        return True

    def find(self, obj):
        for i, x in enumerate(self.array):
            if x == obj:
                return i

        raise ValueError("Object not found in Array")
