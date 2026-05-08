class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)
        l = 0
        r = n*m - 1
        while l <= r:
            mid = (r+l)//2
            i, j = mid//n, mid%n

            if matrix[i][j] == target:
                return True

            elif matrix[i][j] > target:
                r = mid - 1

            else:
                l = mid + 1

        return False