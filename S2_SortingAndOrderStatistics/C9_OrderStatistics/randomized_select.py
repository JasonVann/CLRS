import random

def randomized_select(A, p, r, i):
    '''
    Select the i-th smallest element from A[p..r]
    '''
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if k == i:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q -  1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)

def randomized_partition(A, l, r):
    '''
    To improve performance over presorted array, we randomly pick one item as pivot
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

    sample = random.randint(l, r)
    A[r], A[sample] = A[sample], A[r]
    return pick_last()

def test():
    A = [3, 4, 2, 0, -3, 6]
    res = randomized_select(A, 0, 5, 0)
    print(res)

test()
