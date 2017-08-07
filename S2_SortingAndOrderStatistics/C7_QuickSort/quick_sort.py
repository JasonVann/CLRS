import random

def quick_sort(A, l, r, rand=True):
    '''
    quick sort the given section of list, as instructed in CLRS C7
    To sort the whole list: quick_sort(A, 0, n-1)
    param: l, r are indices of first and last item of the given region
    '''
    if l < r:
        if rand:
            pivot = randomized_partition(A, l, r)
        else:
            pivot = partition(A, l, r)

        quick_sort(A, l, pivot - 1)
        quick_sort(A, pivot + 1, r)

def partition(A, l, r):
    '''
    Default to use the final item as the pivot item
    After partition, items no larger than the pivot will be to the left of the
        pivot item
    return the index of pivot
    '''
    pivot = r
    i = l - 1 # the index of the last item that is no larger than pivot
    j = l  # j - 1 is the index of the last item that is larger than pivot
    for j in range(l, r):
        if A[j] <= A[pivot]:
            A[i+1], A[j] = A[j], A[i+1]
            i += 1
    A[pivot], A[i+1] = A[i+1], A[pivot]
    return i + 1

def randomized_partition(A, l, r):
    '''
    To improve performance over presorted array, we randomly pick one item as pivot
    '''
    sample = random.randint(l, r)
    A[r], A[sample] = A[sample], A[r]
    return partition(A, l, r)

def test():
    A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    quick_sort(A, 0, len(A) - 1)
    print(A)
