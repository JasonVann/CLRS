"""
From CLRS C4
Find the max subarray
"""

def find_max_crossing_subarray(A, low, mid, high):
    """
    Given part of array A[low, high], find the max subarray that cross the mid point
    Left subarray: A[low, mid]
    Right subarray: A[mid+1, high]
    Assumes this part of array has at least 2 elements
    Returns:
        leftmost index of the max crossing subarray
        rightmost index of the max crossing subarray
        the sum of the max crossing subarray
    """
    if low >= high:
        raise Exception("low must be smaller than high!")

    if mid + 1 > high:
        raise Exception("The right subarray cannot be empty! mid + 1 <= high")

    left_sum = None
    temp_sum = 0
    for i in range(mid, low-1, -1):
        temp_sum += A[i]
        if left_sum is None or temp_sum > left_sum:
            left_sum = temp_sum
            left_i = i

    right_sum = None
    temp_sum = 0
    for i in range(mid+1, high+1, 1):
        temp_sum += A[i]
        if right_sum is None or temp_sum > right_sum:
            right_sum = temp_sum
            right_i = i
    return left_i, right_i, left_sum + right_sum


def find_max_subarray(A, low, high):
    """
    Find the max subarray of A[low, high]
    Returns:
        leftmost index of the max crossing subarray
        rightmost index of the max crossing subarray
        the sum of the max crossing subarray
    """
    if low == high:
        # Only one element
        return low, high, A[low]
    mid = int((low + high)/2)
    (left_l, left_r, left_sum) = find_max_subarray(A, low, mid)
    (right_l, right_r, right_sum) = find_max_subarray(A, mid + 1, high)

    (cross_l, cross_r, cross_sum) = find_max_crossing_subarray(A, low, mid, high)

    max_sum = max(left_sum, right_sum, cross_sum)
    if max_sum == left_sum:
        return left_l, left_r, left_sum
    elif max_sum == right_sum:
        return right_l, right_r, right_sum
    else:
        return cross_l, cross_r, cross_sum
