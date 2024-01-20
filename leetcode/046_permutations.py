class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # base case
        if len(nums) == 1:
            return [[nums[0]]]
        
        # res stores the final permutations as we find them
        res = []
        for _ in range(len(nums)):
            # in this iteration, we are generating all permutations 
            # ending in n
            n = nums.pop(0) 
            
            # generate permutations of nums without n
            perms = self.permute(nums)

            for perm in perms:
                # create each of the permutations ending in n
                perm.append(n)
            
            # add to final result
            res.extend(perms)
            
            # add n to the end of nums
            # the next iteration will fetch the first element
            # in this way, we iterate through all elements of nums
            nums.append(n)

        return res