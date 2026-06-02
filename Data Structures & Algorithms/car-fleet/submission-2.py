class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0], reverse=True)
        curFleetTime = 0

        for position, speed in cars:
            destinationTime = (target - position) / speed
            if destinationTime > curFleetTime:
                fleets += 1
                curFleetTime = destinationTime
        return fleets