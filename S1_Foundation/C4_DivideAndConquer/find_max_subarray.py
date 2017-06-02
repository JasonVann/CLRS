"""
From CLRS C4
Find the max subarray
"""

def find_max_crossing_subarray(A, low, mid, high):
    """
    Given part of array A[low, high], find the max subarray that cross the mid point in O(nlogn)
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

def find_max_subarray_linear(A, low, high):
    """
        Find the max subarray in O(n)
        # Also listed as Ex4.1-5
        :param A: array
        :param low: leftmost index of the array
        :param high: rightmost index of the array
        :return: 
            leftmost index of the max crossing subarray
            rightmost index of the max crossing subarray
            the sum of the max crossing subarray
    """

    # nums = A
    # A = [nums[0]]
    # for i in range(1, len(nums)):
    #     A.append(max(A[i - 1] + nums[i], nums[i]))
    # return max(A)

    max_ending_here = max_so_far = A[low]

    meh_l = low
    meh_r = low
    msf_l = low
    msf_r = low

    for i in range(low+1, high + 1):
        if max_ending_here >= 0:
            meh_r = i
            max_ending_here = max_ending_here + A[i]
        else:
            meh_l = i
            meh_r = i
            max_ending_here = A[i]
        if max_so_far <= max_ending_here:
            msf_l = meh_l
            msf_r = meh_r
            max_so_far = max_ending_here
    return (msf_l, msf_r, max_so_far)


if __name__ == 'find_max_subarray':
    print('Running as an imported module!')

if __name__ == '__main__':
    print('Running as a standalone program')