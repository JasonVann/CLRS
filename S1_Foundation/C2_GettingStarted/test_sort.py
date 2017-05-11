import random

max_num = 1e6

def gen_test(n = 1000, max_num = max_num):
    # Generate a list of n items randomly, each number is within +/- of max_num
    n = int(n)
    data = [random.randint(-max_num, max_num) for i in range(n)]
    return data

def verify_sort(data):
    # Verify that the data is sorted ascendingly
    n = len(data)
    for i in range(n-1):
        if data[i] > data[i+1]:
            return False
    return True
