class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        start=1
        end=max(nums)
        while start < end:
            mid = (end+start)//2
            if sum([(i-1)//mid for i in nums]) > maxOperations:
                start = mid+1
            else:
                end = mid
        return (start)