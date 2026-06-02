class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars)
        print(cars)
        fleets = curTime = 0
        while cars:
            position, speed = cars.pop()
            arrTime = (target - position) / speed
            if arrTime > curTime:
                fleets += 1
                curTime = arrTime
        return fleets