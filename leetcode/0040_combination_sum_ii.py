class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        found = set()
        res = []
        combination = []
        C = len(candidates)

        def dfs(i, current_sum):
            if current_sum == target:
                if tuple(combination) not in found:
                    res.append(combination.copy())
                    found.add(tuple(combination))
                return
            
            if current_sum > target or i >= C:
                return

            combination.append(candidates[i])
            dfs(i+1, current_sum + candidates[i])

            combination.pop()
            dfs(i+1, current_sum)

        dfs(0,0)
        return res
        