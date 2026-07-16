class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])
        output = []

        def minLength(query: int) -> int:
            length = float("inf")
            for interval in intervals:
                if interval[0] <= query <= interval[1]:
                    length = min(interval[1] - interval[0] + 1, length)
            return length if length < float("inf") else -1

        for i in range(len(queries)):
            output.append(minLength(queries[i]))
        return output
