from test_sort import *

def selection_sort(data):
    n = len(data)
    for i in range(0, n-1):
        # Find the i-th minimum number and swap with data[i]
        min_i = None
        for j in range(i, n):
            if min_i is None or data[j] < min_i:
                min_i = data[j]
                idx = j
        data[i], data[idx] = data[idx], data[i]

def selection_sort_clrs(data):
    n = len(data)
    for i in range(0, n-1):
        smallest = i
        for j in range(i+1, n):
            if data[j] < data[smallest]:
                smallest = j
        data[i], data[smallest] = data[smallest], data[i]
        
data = gen_test()
#selection_sort(data)
selection_sort_clrs(data)
print(verify_sort(data))

