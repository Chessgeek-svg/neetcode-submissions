class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, reverse = True)
        print(cars)
        fleets = curTime = 0
        for position, speed in cars:
            arrTime = (target - position) / speed
            if arrTime > curTime:
                fleets += 1
                curTime = arrTime
        return fleets