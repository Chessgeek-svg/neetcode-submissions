class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand.sort()
        count = Counter(hand)
        for card in hand:
            if count[card]:
                for i in range(groupSize):
                    count[card+i] -= 1
                    if count[card+i] < 0:
                        return False
        return True