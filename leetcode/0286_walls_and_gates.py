class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        gates = []

        # BFS starting from each gate
        def bfs(i, j, dist):
            # update each space if the distance from the current gate
            q = deque([])
            q.append((i+1, j, dist+1))
            q.append((i-1, j, dist+1))
            q.append((i, j+1, dist+1))
            q.append((i, j-1, dist+1))
            while q:
                r, c, dist = q.popleft()
                
                if (
                    r < 0 or 
                    r >= ROWS or 
                    c < 0 or 
                    c >= COLS or 
                    rooms[r][c] == -1 or 
                    (rooms[r][c] >= 0 and rooms[r][c] <= dist)
                ):
                    continue

                rooms[r][c] = dist  
                q.append((r+1, c, dist+1))
                q.append((r-1, c, dist+1))
                q.append((r, c+1, dist+1))
                q.append((r, c-1, dist+1))

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    bfs(r, c, 0)
        
        return rooms

        

        
        