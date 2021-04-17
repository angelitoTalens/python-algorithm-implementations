import unittest
from hashmap import HashMap

class HashMapTest(unittest.TestCase):
    def test_put_get(self):
        hash_map = HashMap()
        for key in range(1, 21):
            value = key * 2
            hash_map.put(key, value)
            self.assertEqual(hash_map.get(key), value)
    
    def test_put_size(self):
        hash_map = HashMap()
        size = 20
        for key in range(1, size + 1):
            value = key * 2
            hash_map.put(key, value)
        
        self.assertEqual(hash_map.size(), size)

        for key in range(1, size + 1):
            value = key * 2
            hash_map.put(key, value)

        self.assertEqual(hash_map.size(), size)


    def test_put_remove(self):
        hash_map = HashMap()
        size = 20
        for key in range(1, size + 1):
            value = key * 2
            hash_map.put(key, value)
        
        self.assertEqual(hash_map.size(), size)

        for key in range(1, size + 1):            
            hash_map.remove(key)

        self.assertEqual(hash_map.size(), 0)

if __name__ == "__main__":
    unittest.main()