from max_heapify import *

def Ex6_2_1():
    A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    heap = Heap.Heap(A)
    print(heap.data)
    max_heapify(heap, 2)
    print(heap.data)

Ex6_2_1()
