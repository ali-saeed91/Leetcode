class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapify(nums)
    
        while k >0:
            x=heappop(nums)
            heappush(nums,-x)
            k -=1
        # print(nums)
        return sum(nums)