class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(left, right, s):
            if len(s) == 2 * n:
                res.append(s)
                return
            
            if left < n:
                dfs(left + 1, right, s + "(")
            
            if right < left:
                dfs(left, right + 1, s + ")")
        
        dfs(0, 0, "")
        return res