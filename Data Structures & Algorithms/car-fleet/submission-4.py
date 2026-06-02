class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed)) #generator not lis
        cars.sort(key = lambda x : x[0])

        finishTime = fleets = 0
        while cars:
            position, speed = cars.pop()
            curFinishTime = (target - position) / speed
            if curFinishTime > finishTime:
                fleets += 1
                finishTime = curFinishTime
        return fleets