class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 ==1 : return False
        else : half = total // 2 
        cache = {} 
        def helper(i,target):
            if i >= len(nums):
                if target == 0:
                    return True
                return False
            if (i,target) in cache:
                return cache[(i,target)]
            cache[(i,target)] = helper(i+1, target) or helper(i+1, target - nums[i])
            return cache[(i,target)]
        return helper(0,half)