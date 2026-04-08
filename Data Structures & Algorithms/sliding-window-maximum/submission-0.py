class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        l = 0
        for r in range(k):
            heapq.heappush(heap, (-nums[r], r))

        res.append(-heap[0][0])

        for r in range(k, len(nums)):
            l+=1
            heapq.heappush(heap, (-nums[r], r))
            while heap[0][1]<l:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res