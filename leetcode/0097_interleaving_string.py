class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        ROWS, COLS = len(s1) + 1, len(s2) + 1
        dp = [[None] * COLS for _ in range(ROWS)]

        dp[0][0] = True
        for c in range(1, COLS):
            dp[0][c] = dp[0][c-1] and s3[c-1] == s2[c-1]
        for r in range(1, ROWS):
            dp[r][0] = dp[r-1][0] and s3[r-1] == s1[r-1]
        
        for c in range(1, COLS):
            for r in range(1, ROWS):
                dp[r][c] = (
                    (dp[r-1][c] and s3[r+c-1] == s1[r-1]) or
                    (dp[r][c-1] and s3[r+c-1] == s2[c-1])
                )
        
        return dp[-1][-1]