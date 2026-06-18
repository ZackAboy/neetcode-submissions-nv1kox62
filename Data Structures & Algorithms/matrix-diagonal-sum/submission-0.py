class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)
        for i in range(n):
            if i != n-1-i:
                sum += mat[i][n-1-i]
            sum += mat[i][i]
        return sum