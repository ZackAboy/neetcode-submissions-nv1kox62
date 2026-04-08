class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for num, val in freq.items():
            heapq.heappush(heap, (val,num))
            if len(heap)>k:
                heapq.heappop(heap)

        return [i[1] for i in heap]