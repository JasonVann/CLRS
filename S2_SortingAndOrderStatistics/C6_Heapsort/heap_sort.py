from build_max_heap import *

def heap_sort(A:list):
    heap = Heap.Heap(A)
    build_max_heap(heap)
    n = heap.size
    for i in range(n - 1, 0, -1):
        # Stop when there's only one item in the heap
        A[i], heap.data[0] = heap.data[0], A[i]
        heap.size -= 1
        max_heapify(heap, 0)

def test_heap_sort():
    A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    A = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    print(A)
    heap_sort(A)
    print(A)

test_heap_sort()
