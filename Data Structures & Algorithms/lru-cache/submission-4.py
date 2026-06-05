class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.least, self.most = Node(0,0), Node(0,0)
        self.least.next, self.most.prev = self.most, self.least

    def insert(self, node):
        node.next, node.prev = self.most, self.most.prev
        self.most.prev.next = node
        self.most.prev = node

    def remove(self, node):
        nxt, prev = node.next, node.prev
        nxt.prev, prev.next = prev, nxt
        #del node #IDK correct way to remove

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(self.cache[key]) #walrus operator for one liner?
        if len(self.cache) > self.cap:
            lru = self.least.next
            self.remove(lru)
            del self.cache[lru.key]

        
