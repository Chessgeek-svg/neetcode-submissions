class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for letter in tasks:
            counts[letter] = counts.get(letter, 0) + 1
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)
        time = 0
        cooldown = deque()
        while maxHeap or cooldown:
            if not maxHeap:
                time = cooldown[0][1]
            else:
                count = heapq.heappop(maxHeap) + 1
                if count < 0:
                    cooldown.append([count, time + n])
                
            if cooldown and time == cooldown[0][1]:
                count, _ = cooldown.popleft()
                heapq.heappush(maxHeap, count)
            
            time += 1
        return time