class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        n = len(speed)
        for i in range (n):
            car.append([position[i], speed[i]])
        car.sort(reverse = True)

        time = 0
        fleets = 0
        for p, s in car:
            t = (target - p)/s
            if t > time:
                fleets += 1
                time = t
        return fleets