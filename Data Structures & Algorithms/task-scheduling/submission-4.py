class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        for char, count in freq.items():
            heap.append((-count, char))
        
        heapq.heapify(heap)

        q = deque()
        time = 0

        while heap or q:

            if heap:
                time += 1
                count, char = heapq.heappop(heap)
                count +=1
                if count < 0:
                    q.append((time+n, count, char))

            if q:
                if not heap:
                    time = q[0][0]

                while q and time >= q[0][0]:
                    x, count, char = q.popleft()
                    heapq.heappush(heap, (count, char))

        return time