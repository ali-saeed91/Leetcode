class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        base = nums[0]
        if len(nums) == 1:
            return base
        x = base
        y =0
        for i in range(1,len(nums)):
            x = min(abs(x), abs(nums[i]))
        
        if x not in nums:
            x = -1 * x
            return (x)
        else:
            return (x)