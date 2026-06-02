class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        stack = sorted(cars)

        curArrivalTime = fleets = 0
        while stack:
            position, speed = stack.pop()
            arrivalTime = (target - position) / speed
            if arrivalTime > curArrivalTime:
                fleets += 1
                curArrivalTime = arrivalTime
        return fleets