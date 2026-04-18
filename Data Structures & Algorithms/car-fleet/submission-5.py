class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(speed)):
            cars.append((position[i],speed[i]))

        cars.sort()

        curr = None
        res = 0

        while cars:
            pos, speed = cars.pop()
            time = (target-pos)/speed
            if not curr or curr < time:
                curr = time
                res+=1

        return res