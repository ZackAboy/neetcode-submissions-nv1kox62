class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            val = a-b
            if val:
                heapq.heappush(heap,-val)

        return -heap[0] if heap else 0