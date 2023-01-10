class Solution:
    def findMin(self, nums: List[int]) -> int:
        heapify(nums)
        return nums[0]