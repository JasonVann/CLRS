import unittest
from find_max_subarray import *

class TestMaxSubarray(unittest.TestCase):
    def setUp(self):
        self.A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        self.short = [3, 4]

    def test_exception(self):
        # msg can be used if used with context manager
        with self.assertRaises(Exception, msg="Testing"):
            find_max_crossing_subarray(self.A, 2,2,1)

    def test_max_subarray(self):
        (l, r, temp_sum) = find_max_subarray(self.A, 0, len(self.A) - 1)
        self.assertEqual((l, r, temp_sum), (7, 10, 43))

    def test_max_subarray_linear(self):
        (l, r, temp_sum) = find_max_subarray_linear(self.A, 0, len(self.A) - 1)
        self.assertEqual((l, r, temp_sum), (7, 10, 43))

    def test_max_subarray2(self):
        (l, r, temp_sum) = find_max_subarray(self.short, 0, len(self.short) - 1)
        self.assertEqual((l, r, temp_sum), (0, 1, 7))

    def test_max_subarray3(self):
        A = [3]
        (l, r, temp_sum) = find_max_subarray(A, 0, len(A) - 1)
        self.assertEqual((l, r, temp_sum), (0, 0, 3))

    def test_neg(self):
        A = [-1, -2, -3]
        (l, r, temp_sum) = find_max_subarray(A, 0, len(A) - 1)
        self.assertEqual((l, r, temp_sum), (0, 0, -1))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMaxSubarray('test_exception'))
    return suite

if __name__ == '__main__':
    unittest.main()
