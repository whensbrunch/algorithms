class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Approach: BFS starting at edges
        # Keep two sets, pacific and atlantic, for indices that can flow to
        # each ocean (i.e. that can be reached from the edges)
        # Keep a set for visited nodes

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def bfs(r, c, seen, prev_height):
            q = deque([(r, c, prev_height)])
            
            while q:
                r, c, prev_height = q.popleft()
                if (
                    (r < 0 or r >= ROWS or c < 0 or c >= COLS) or 
                    (r, c) in seen or
                    heights[r][c] < prev_height
                ):
                    continue
                
                seen.add((r, c))
                q.append((r+1, c, heights[r][c]))
                q.append((r-1, c, heights[r][c]))
                q.append((r, c+1, heights[r][c]))
                q.append((r, c-1, heights[r][c]))

        for c in range(COLS):
            bfs(0, c, pac, float("-inf"))
            bfs(ROWS-1, c, atl, float("-inf"))
        
        for r in range(ROWS):
            bfs(r, 0, pac, float("-inf"))
            bfs(r, COLS-1, atl, float("-inf"))
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
            