import unittest
from binarysearch import binarysearch

class BinarySearchTest(unittest.TestCase):
    def setUp(self):
        self.arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def test_search_middle_item(self):        
        self.assertEqual(binarysearch(self.arr, 0, len(self.arr) - 1, 5), 5)
    
    def test_search_upper_end_item(self):        
        self.assertEqual(binarysearch(self.arr, 0, len(self.arr) - 1, 9), 9)
    
    def test_search_lower_end_item(self):        
        self.assertEqual(binarysearch(self.arr, 0, len(self.arr) - 1, 0), 0)

    def test_search_not_existing_item(self):        
        self.assertEqual(binarysearch(self.arr, 0, len(self.arr) - 1, 20), None)
    
    def test_single_element_array(self): 
        arr = [1]       
        self.assertEqual(binarysearch(arr, 0, len(arr) - 1, 1), 0)
    
    def test_even_element_array(self): 
        arr = [0, 1]       
        self.assertEqual(binarysearch(arr, 0, len(arr) - 1, 1), 1)
    
    def test_odd_element_array(self): 
        arr = [0, 1, 2]       
        self.assertEqual(binarysearch(arr, 0, len(arr) - 1, 1), 1)

if __name__ == "__main__":
    unittest.main()