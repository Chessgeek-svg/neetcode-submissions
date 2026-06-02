class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)
        used = [False] * len(hand)
        while not used[-1]:
            size = 0
            next_val = 0
            for i in range(len(hand)):
                if used[i]:
                    continue
                if size == 0:
                    size += 1
                    next_val = hand[i] + 1
                    used[i] = True
                else:
                    if hand[i] == next_val:
                        size += 1
                        next_val += 1
                        used[i] = True
                if size == groupSize:
                    break
            if size != groupSize:
                return False
        return all(used)
