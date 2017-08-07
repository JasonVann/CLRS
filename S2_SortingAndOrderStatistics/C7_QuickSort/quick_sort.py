import random

def quick_sort(A, l, r, partition_type="rand"):
    '''
    quick sort the given section of list, as instructed in CLRS C7
    To sort the whole list: quick_sort(A, 0, n-1)
    param: l, r are indices of first and last item of the given region
    '''
    if l < r:
        pivot = partition(A, l, r, partition_type)
        quick_sort(A, l, pivot - 1, partition_type)
        quick_sort(A, pivot + 1, r, partition_type)

def partition(A, l, r, partition_type = 'rand'):
    '''
    Calls different partition algorithm by the given partition_type
    params: partition_type
        'rand', 'hoare', 'last'
    '''
    def pick_last():
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

    def hoare_partition(A, l, r):
        '''
        The original partition algorithm from Hoare
        Every element in [l..j] <= every element in A[j+1...r]
        '''
        pivot_val = A[l]
        i = l
        j = r
        while True:
            while A[j] > pivot_val:
                j = j - 1
            while A[i] < pivot_val:
                i = i + 1
            if i < j:
                A[i], A[j] = A[j], A[i]
            else:
                return j

    if partition_type == 'rand':
        pivot = randomized_partition(A, l, r)
    elif partition_type == 'hoare':
        pivot = hoare_partition(A, l, r)
    else:
        pivot = pick_last(A, l, r)
    return pivot

def test():
    A = [19, 13, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    quick_sort(A, 0, len(A) - 1, partition_type = 'hoare')
    print(A)

def Ex7_1():
    A = [19, 13, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    partition(A, 0, len(A) - 1, 'hoare')
    print(A)
