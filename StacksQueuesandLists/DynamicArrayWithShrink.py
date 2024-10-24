# 3-3. [5] We have seen how dynamic arrays enable arrays to grow while still achieving
#   constant-time amortized performance. This problem concerns extending dynamic
#   arrays to let them both grow and shrink on demand.
# (a) Consider an underflow strategy that cuts the array size in half whenever the
#     array falls below half full. Give an example sequence of insertions and deletions
#     where this strategy gives a bad amortized cost.
# (b) Then, give a better underflow strategy than that suggested above, one that
#     achieves constant amortized cost per deletion.
import math

from DataStructures.DynamicArray import DynamicArray

class DynamicArrayWithShrink(DynamicArray):
    def shrink(self):
        self.capacity = math.ceil(self.capacity/2)
        new_arr = [None] * self.capacity

        for i in range(self.capacity):
            new_arr[i] = self.array[i]

        self.array = new_arr

    def pop(self):
        if self.size-1 <= self.capacity/4:
            self.shrink()

        return super().pop()

    def remove_first(self):
        if self.size-1 <= self.capacity/4:
            self.shrink()

        return super().remove_first()

    def remove_index(self, index):
        if self.size-1 <= self.capacity/4:
            self.shrink()

        return super().remove_index(index)

    def remove(self, obj):
        if self.size-1 <= self.capacity/4:
            self.shrink()

        return super().remove(obj)