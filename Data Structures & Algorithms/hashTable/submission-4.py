class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val
    
class HashTable:
    
    def __init__(self, capacity: int):
        self.map = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def hashFunction(self, key: int):
        print(key, self.capacity, key % self.capacity)
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        hashKey = self.hashFunction(key)
        while self.map[hashKey]:
            if key == self.map[hashKey].key:
                self.map[hashKey].val = value
                return
            hashKey = (hashKey + 1) % self.capacity
        
        self.map[hashKey] = Pair(key, value)
        self.size += 1
        
        if self.size * 2 >= self.capacity:
            self.resize()


    def get(self, key: int) -> int:
        hashKey = self.hashFunction(key)
        while self.map[hashKey]:
            if key == self.map[hashKey].key:
                return self.map[hashKey].val
            hashKey = (hashKey + 1) % self.capacity
        return -1


    def remove(self, key: int) -> bool:
        hashKey = self.hashFunction(key)
        while self.map[hashKey]:
            if key == self.map[hashKey].key:
                self.map[hashKey] = Pair(None, None)
                self.size -= 1
                return True
            hashKey = (hashKey + 1) % self.capacity
        return False



    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self. capacity *= 2
        newMap = [None] * self.capacity
        
        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.insert(pair.key, pair.val)


