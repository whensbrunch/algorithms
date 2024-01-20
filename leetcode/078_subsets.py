class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        
        inc = [[nums[0]] + subset for subset in self.subsets(nums[1:])]
        exc = self.subsets(nums[1:])

        return inc + exc