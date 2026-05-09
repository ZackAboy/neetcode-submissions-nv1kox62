class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.time[key]) - 1
        res = ""
        while l <= r:
            mid = (l+r)//2

            if self.time[key][mid][0] <= timestamp:
                res = self.time[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res