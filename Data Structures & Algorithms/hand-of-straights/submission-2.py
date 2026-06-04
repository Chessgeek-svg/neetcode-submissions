class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        counts = Counter(hand)
        hand = sorted(hand)
        for card in hand:
            if counts[card]:
                for i in range(groupSize):
                    if counts[card +i] <= 0:
                        return False
                    counts[card + i] -= 1
        return True
        