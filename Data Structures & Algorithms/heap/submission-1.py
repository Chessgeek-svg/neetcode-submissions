class MinHeap:
    
    def __init__(self):
        self.heap = [0]
        
    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) -1

        while i > 1:
            if self.heap[i] < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
                i = i//2
            else:
                break


    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        val = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.bubbleDown(1)
        return val
        
    def bubbleDown(self, i: int):
        while i * 2 < len(self.heap):
            if i * 2 + 1 < len(self.heap) and self.heap[i] > self.heap[i*2+1] and self.heap[i * 2 + 1] < self.heap[i * 2]:
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                i = i * 2 + 1
            elif self.heap[i] > self.heap[i*2]:
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2
            else:
                break

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1
        

    def heapify(self, nums: List[int]) -> None:
        self.heap += nums
        for i in range(len(self.heap)//2, -1, -1):
            self.bubbleDown(i)        