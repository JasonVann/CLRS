def counting_sort(A):
    '''
    Implementation fo counting sort in CLRS C8.2
    params: A: unsorted list, assuming nonnegative element
    Returns sorted list B
    '''
    k = max(A) + 1
    C = [0] * k
    n = len(A)
    B = [0] * n

    for i in range(n):
        # Let C[i] holds the count of occurences of i
        C[A[i]] += 1

    # Let C[i] holds the count of numbers <= i
    for i in range(1, k):
        C[i] += C[i-1]

    for i in range(n-1, -1, -1):
        number = A[i]
        count = C[number] - 1 # Subtract 1 as the list is 0-based
        B[count] = number
        C[number] -= 1
    print('input:', A)
    print('sorted:', B)
    return B

def test():
    A = [2,5,3,0,2,3,0,3]
    counting_sort(A)

#test()

def ex8_2_1():
    A = [6,0,2,0,1,3,4,6,1,3,2]
    counting_sort(A)

ex8_2_1()
