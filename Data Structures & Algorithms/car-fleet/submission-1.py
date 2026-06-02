class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []

        for position, speed in cars:
            destinationTime = (target-position) / speed
            stack.append(destinationTime)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
