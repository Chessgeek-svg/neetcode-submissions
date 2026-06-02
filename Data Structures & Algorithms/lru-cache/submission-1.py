class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.history = [] 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.updateHistory(key)
            return self.cache[key]  
        return -1
        

    def put(self, key: int, value: int) -> None:
        print(self.history)
        if key not in self.cache:
            self.history.append(key)
            if len(self.history) > self.capacity:
                deleteKey = self.history.pop(0)
                del self.cache[deleteKey]
            self.cache[key] = value
            return

        self.cache[key] = value
        self.updateHistory(key)
    
    def updateHistory(self, key: int):
        index = self.history.index(key)
        for i in range(index, len(self.history)-1, 1):
            self.history[i] = self.history[i+1]
        self.history[-1] = key


        
