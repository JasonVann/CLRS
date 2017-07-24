#For Ex6.2-2
import Heap

def min_heapify(A:Heap, i):
    '''
    Maintains the min heap property: A[i] <= A[left(i)] && A[i] <= A[right(i)]
    '''
    if i >= A.size or i < 0:
        raise "i is not a valid index"

    left = A.left(i)
    right = A.right(i)
    smallest = i
    if left is not None and A.data[left] <= A.data[i]:
        smallest = left
    if right is not None and A.data[right] <= A.data[smallest]:
        smallest = right
    if i != smallest:
        # Then min heap property is violated
        A.data[smallest], A.data[i] = A.data[i], A.data[smallest]
        min_heapify(A, smallest)

def test_min_heapify():
    A = [1,13,5,7,9,11,13,15,17]
    heap = Heap.Heap(A)
    print(heap.data)
    min_heapify(heap, 1)
    print(heap.data)

#test_min_heapify()
