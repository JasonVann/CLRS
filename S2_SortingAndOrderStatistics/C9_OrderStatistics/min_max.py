def min_max(A, n):
    '''
    Find the min and max of a list A, assuming the number of elements is given
    '''
    if n <= 0:
        raise Exception("List cannot be empty")

    if n % 2 == 0:
        min_val = min(A[0], A[1])
        max_val = max(A[0], A[1])
        i = 2
    else:
        min_val = A[0]
        max_val = A[0]
        i = 1
    while i < n - 1:
        if A[i] > A[i+1]:
            temp_max = A[i]
            temp_min = A[i+1]
        else:
            temp_max = A[i+1]
            temp_min = A[i]
        if temp_max > max_val:
            max_val = temp_max
        if temp_min < min_val:
            min_val = temp_min
        i += 1
    return min_val, max_val

def test():
    A = [1,1,2,3,4,0, 4]
    res = min_max(A, 7)
    print(res)

test()
