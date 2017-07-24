from build_max_heap import *

def ex6_3_1():
    A = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    heap = Heap.Heap(A)
    print(heap.data)
    build_max_heap(heap)
    print(heap.data)

ex6_3_1()
