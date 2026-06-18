class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = defaultdict(list)
        for num, freq in Counter(nums).items():
            buckets[freq].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
