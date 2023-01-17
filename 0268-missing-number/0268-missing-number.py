class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        while i < len(nums):
            pos = nums[i]
            if pos < len(nums) and pos != i:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i +=1

        for j in range(len(nums)):
            if nums[j] != j:
                return (j)
            
        return (len(nums))