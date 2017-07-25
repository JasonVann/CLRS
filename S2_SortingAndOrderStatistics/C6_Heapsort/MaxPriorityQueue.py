from build_max_heap import *
from Heap import *

class MaxPriorityQueue(Heap):
    def __init__(self, A:list):
        Heap.__init__(self, A)

    @property
    def heap_maximum(self):
        return self.data[0]

    def heap_extract_max(self):
        '''
        Removes and returns the element of S with the largest key
        '''
        if self.size < 1:
            raise "Heap underflow"

        maximum = self.data[0]
        self.data[0] = self.data[self.size - 1]
        self.size -= 1
        max_heapify(self, 0)
        return maximum

    def heap_increase_key(self, i, key):
        '''
        Increases the value of i to the new key k
        Assums k >= i
        '''
        A = self.data
        if key < A[i]:
            raise "new key is smaller than current key"

        A[i] = key

        while i > 0 and A[self.parent(i)] < A[i]:
            A[i], A[self.parent(i)] = A[self.parent(i)], A[i]
            i = self.parent(i)

    def max_heap_insert(self, key):
        '''
        Inserts the key to the pq
        '''
        self.size += 1
        self.data.append(float('-inf'))
        self.heap_increase_key(self.size - 1, key)

    def max_heap_delete(self, i):
        '''
        Deletes node i
        For Ex6.5-8
        '''
        if i < 0 or i >= self.size:
            raise "Invalid index"

        A = self.data
        A[i] = A[self.size - 1]
        # Now the last item has been duplicated, delete the original one
        A.pop(self.size - 1)
        self.size -= 1
        max_heapify(self, i)
