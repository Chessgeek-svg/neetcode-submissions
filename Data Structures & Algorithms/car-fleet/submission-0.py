class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p, s in zip(position, speed)]
        curtime = fleets = 0

        for position, speed in sorted(cars, reverse = True):
            destinationTime = (target-position) / speed
            if curtime < destinationTime:
                fleets += 1
                curtime = destinationTime
        return fleets
