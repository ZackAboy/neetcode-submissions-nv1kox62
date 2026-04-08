class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for n, f in freq.items():
            heapq.heappush(heap, (f, n))
            if len(heap)>k:
                heapq.heappop(heap)

        return [i[1] for i in heap]
