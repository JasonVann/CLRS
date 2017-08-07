# For CLRS Ex7.1-1
from quick_sort import *

A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]

pivot = partition(A, 0, len(A) - 1)
print(pivot, A)
