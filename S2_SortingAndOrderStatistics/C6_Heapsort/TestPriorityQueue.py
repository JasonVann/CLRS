import unittest
from MaxPriorityQueue import *

class TestingPQ(unittest.TestCase):
    def setUp(self):
        self.A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]

    def test_max_pq(self):
        # Ex6.5-1
        A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
        max_pq = MaxPriorityQueue(A)
        #print(A[0])
        ans = max_pq.heap_extract_max()
        #print(A[0])
        self.assertEqual(ans, 15)
        self.assertEqual(A[0], 13)

    def test_heap_increase_key(self):
        A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        max_pq = MaxPriorityQueue(A)
        print("Prior to increase key: {}".format(A))
        max_pq.heap_increase_key(8, 15)
        print("After increasing key: {}".format(A))
        self.assertEqual(A, [16, 15, 10, 14, 7, 9, 3, 2, 8, 1])

    def test_max_heap_insert(self):
        # 6.5-2
        A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
        max_pq = MaxPriorityQueue(A)
        print("Prior to insert: {}".format(A))
        max_pq.max_heap_insert(10)
        print("After inserting: {}".format(A))
        self.assertEqual(A, [15, 13, 10, 5, 12, 9, 7, 4, 0, 6, 2, 1, 8])

if __name__ == '__main__':
    unittest.main()
