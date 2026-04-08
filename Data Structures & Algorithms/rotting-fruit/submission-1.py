class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = set()
        q = deque()
        fresh = list()

        def rot(r, c):
            if r<0 or r>=m or c<0 or c>=n or (r, c) in visit or grid[r][c] == 0:
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    fresh.append([r, c])
        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    fresh.remove([r, c])
                rot(r+1, c)
                rot(r-1, c)
                rot(r, c+1)
                rot(r, c-1)
            if q:
                time += 1
        
        if not fresh:
            return time
        else:
            return -1