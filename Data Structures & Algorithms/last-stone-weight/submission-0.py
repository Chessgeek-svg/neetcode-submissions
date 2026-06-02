class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            print(stones)
            temp = stones.pop()
            stones[-1] = temp - stones[-1]
            if stones[-1] == 0:
                stones.pop()
            stones.sort()
        return stones[0] if stones else 0
