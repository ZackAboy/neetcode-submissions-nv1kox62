class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        cars = []

        for i in range(n):
            cars.append((position[i], speed[i]))

        cars.sort(reverse = True)

        fleets = []
        for pos, speed in cars:
            time = (target - pos) / speed
            if not fleets or fleets[-1]<time:
                fleets.append(time)
        
        return len(fleets)