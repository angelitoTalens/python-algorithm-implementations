import unittest
from bubblesort import bubblesort

class BubbleSortTest(unittest.TestCase):
    def setUp(self):
        self.expected_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def test_unsorted_random(self):
        arr = [2, 1, 6, 8, 3, 9, 4, 5, 7]
        bubblesort(arr)
        self.assertEqual(arr, self.expected_arr)
    
    def test_already_sorted(self):
        arr =  [1, 2, 3, 4, 5, 6, 7, 8, 9]        
        bubblesort(arr)
        self.assertEqual(arr, self.expected_arr)

    def test_unsorted_reverse(self):
        arr =  [9, 8, 7, 6, 5, 4, 3, 2, 1]        
        bubblesort(arr)
        self.assertEqual(arr, self.expected_arr)

if __name__ == "__main__":
    unittest.main()