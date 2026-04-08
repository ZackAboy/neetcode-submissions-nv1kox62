class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = []
        for listt in matrix:
            s = s + listt
        l = 0
        r = len(s) - 1
        while l <= r:
            mid = (l + r) // 2
            if s[mid] == target:
                return True
            elif s[mid] > target:
                r = mid -1
            else:
                l = mid +1
        return False