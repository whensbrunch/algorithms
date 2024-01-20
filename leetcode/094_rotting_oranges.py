from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        fresh = 0
        rotten_q = deque([])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten_q.append((r,c))
        
        if fresh == 0:
            return 0
        
        
        min_elapsed = -1
        while rotten_q:
            new_rotten = []
            while rotten_q:
                r, c = rotten_q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    if (
                        r + dr >= 0 and 
                        r + dr < R and
                        c + dc >= 0 and
                        c + dc < C and
                        grid[r+dr][c+dc] == 1
                    ):
                        grid[r+dr][c+dc] = 2
                        fresh -= 1
                        new_rotten.append((r+dr, c+dc))
            rotten_q = deque(new_rotten)
            min_elapsed += 1
        
        return min_elapsed if fresh == 0 else -1

    