class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for card in hand:
            start = card
            while count[start-1]:
                start -= 1
            while start <= card:
                while count[start]:
                    for i in range(groupSize):
                        count[start+i] -= 1
                        if count[start+i] < 0:
                            return False
                start += 1
        return True