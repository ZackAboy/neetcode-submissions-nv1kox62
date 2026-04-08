class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            x = i[0]
            y = i[1]
            dist = (x*x + y*y)
            heapq.heappush(heap, (-dist, [x,y]))
            if len(heap)>k:
                heapq.heappop(heap)

        return [coords for dist, coords in heap]