class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return
            
            if grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        

        num_islands = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)
        
        return num_islands
        
