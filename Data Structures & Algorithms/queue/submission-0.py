class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail 

    def append(self, value: int) -> None:
        newNode = Node(value)
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        lastNode = self.tail.prev
        prevNode = lastNode.prev
        val = lastNode.val

        prevNode.next = self.tail
        self.tail.prev = prevNode

        return val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        firstNode = self.head.next
        nextNode = firstNode.next
        val = firstNode.val

        nextNode.prev = self.head
        self.head.next = nextNode
        
        return val