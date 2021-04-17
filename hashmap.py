class HashMap:
    def __init__(self):
        self.hash_table = [[] for i in range(1, 11)]
        self._size = 0
    
    def hash(self, key: int) -> int:
        return key % len(self.hash_table)

    def put(self, key: int, value: any):
        bucket = self.hash_table[self.hash(key)]

        existing_item = False
        for item in bucket:
            if item[0] == key:
                item[1] = value
                existing_item = True
                break
        
        if not existing_item:
            bucket.append([key, value])
            self._size += 1
        

    def get(self, key):
        bucket = self.hash_table[self.hash(key)]        
        for item in bucket:
            if item[0] == key:
                return item[1]        
        return None

    def remove(self, key: int):
        bucket = self.hash_table[self.hash(key)]
        
        for idx, item in enumerate(bucket):
            if item[0] == key:
                del bucket[idx]
                self._size -= 1
                break
    
    def size(self) -> int:
        return self._size