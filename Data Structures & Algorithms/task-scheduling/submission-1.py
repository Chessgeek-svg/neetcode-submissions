class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while maxHeap or q:
            if not maxHeap:
                time = q[0][1]

            else:
                count = heapq.heappop(maxHeap) + 1
                if count < 0:
                    q.append((count, time + n))
            
            if q and q[0][1] == time:
                count, _ = q.popleft()
                heapq.heappush(maxHeap, count)
            time += 1
        return time