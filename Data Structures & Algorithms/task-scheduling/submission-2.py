class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-cnt for cnt in counts.values()]
        print(maxHeap)
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0
        while maxHeap or queue:
            if maxHeap:
                val = heapq.heappop(maxHeap) + 1
                if val < 0:
                    queue.append((val, time + n))
            else:
                time = queue[0][1]
            if queue and queue[0][1] == time:
                val, _ = queue.popleft()
                heapq.heappush(maxHeap, val)
            time += 1
        return time


