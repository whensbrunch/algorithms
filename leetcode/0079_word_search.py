class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        seen = {}

        def dfs(i, r, c):
            if r < 0 or r >= R or c < 0 or c >= C:  # out of bounds
                return False 
            if board[r][c] != word[i]:  # wrong letter
                return False
            if (r, c) in seen:  # already seen
                return False

            seen[(r,c)] = word[i]
            i += 1
            if i == len(word):
                return True
            
            res = (
                dfs(i, r+1, c) or
                dfs(i, r-1, c) or
                dfs(i, r, c+1) or
                dfs(i, r, c-1)
            )
            seen.pop((r,c))

            return res


        for r in range(R):
            for c in range(C):
                if dfs(0, r, c):
                    return True
        return False