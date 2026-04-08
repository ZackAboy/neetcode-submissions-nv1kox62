class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = []

        for i in range(len(position)):
            ps.append((position[i], speed[i]))

        ps.sort(reverse = True)
        
        stack = []
        for x in ps:
            pos, speed = x
            time = (target-pos)/speed
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)