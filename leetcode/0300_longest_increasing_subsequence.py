class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        max_len = 1

        for i in range(len(nums)):
            curr_max = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    curr_max = max(curr_max, 1 + dp[j])
            dp[i] = curr_max
            max_len = max(max_len, curr_max)

        return max_len