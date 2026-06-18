class Solution:
    def countOdds(self, low: int, high: int) -> int:
        hodds = (high + 1) // 2
        lodds = low // 2
        return hodds - lodds