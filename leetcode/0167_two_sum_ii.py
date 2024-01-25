class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if (numbers[l] + numbers[r]) == target:
                return [l+1, r+1]
            elif (numbers[l] + numbers[r]) < target:
                l += 1
                while l < len(numbers) and numbers[l] == numbers[l-1]:
                    l += 1
            else:
                r -= 1
                while r >= 0 and numbers[r] == numbers[r+1]:
                    r -= 1
        return [-1, -1]