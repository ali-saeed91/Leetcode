class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i=0
        while i < len(nums):
            if nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1] ,nums[i] = nums[i], nums[nums[i]-1]
            else:
                i +=1
        return [j for j in range(1, len(nums)+1) if j != nums[j-1]]    