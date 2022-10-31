class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heappush(maxHeap, -num)
        # print(maxHeap)    
        heapify(maxHeap)
        # print(maxHeap)
        for i in range(k-1):
            heappop(maxHeap)
        # print(maxHeap)
        return -maxHeap[0]  