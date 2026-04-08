class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        cars = []

        for i in range(n):
            cars.append((position[i], speed[i]))

        cars.sort(reverse = True)

        fleets = None
        res = 0
        for pos, speed in cars:
            time = (target - pos) / speed
            if not fleets or fleets<time:
                fleets = time
                res +=1
        
        return res