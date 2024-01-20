# beats 57%
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        
        inc = [[nums[0]] + subset for subset in self.subsets(nums[1:])]
        exc = self.subsets(nums[1:])

        return inc + exc

# beats 98%
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]

        # holds all of the results as we compute them
        res = []

        # holds the current subset we're building
        subset = []

        # dfs builds all subsets of nums[i:]
        def dfs(i):
            # if we've reached the end of the decision tree, add the current subset
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # branch where nums[i] is in the subset
            subset.append(nums[i])
            dfs(i+1)

            # branch where nums[i] is not in the subset
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res