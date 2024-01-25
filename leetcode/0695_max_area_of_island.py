class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Approach: Iterate over matrix and start a BFS from each 1 that we find
        # Keep track of the max island size as we go along

        if len(grid) == 1 and not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            size = 0
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                    continue

                size += 1
                grid[r][c] = 0
                q.append((r+1, c))
                q.append((r-1, c))
                q.append((r, c+1))
                q.append((r, c-1))
            
            return size
            



        max_size = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    size = bfs(r, c)
                    max_size = max(max_size, size)

        return max_size
        