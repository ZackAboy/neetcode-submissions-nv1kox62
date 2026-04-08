class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        res = 0

        for i in operations:
            if i == "+":
                arr.append(int(arr[-1]) + int(arr[-2]))
            elif i == "D":
                arr.append(int(arr[-1])*2)
            elif i == "C":
                arr.pop()
            else:
                arr.append(int(i))

        for num in arr:
            res += num

        return res