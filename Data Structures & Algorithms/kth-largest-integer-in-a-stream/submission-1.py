class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.count = 0
        self.k = k

        for i, num in enumerate(nums):
            heapq.heappush(self.heap, (num, self.count))
            self.count+=1
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, (val, self.count))
        self.count += 1

        if len(self.heap)>self.k:
            heapq.heappop(self.heap)

        return self.heap[0][0]