class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        
        for m in matrix:
            maxHeap.extend(m)
        heapify(maxHeap)
        
        for i in range(k-1):
            heappop(maxHeap)
        return (maxHeap[0])