class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        if len(nums) == 1:
            return nums[0]
        while start <= end:
            mid = start + (end-start)//2
            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[end]: 
                start = mid +1
            else:
                end = mid -1
        return nums[0]