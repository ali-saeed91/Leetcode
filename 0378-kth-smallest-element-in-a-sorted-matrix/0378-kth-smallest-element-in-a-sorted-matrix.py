class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        # print(len(matrix))
        # for a,b,c in matrix:
        for m in matrix:
            # arr +=m
            maxHeap.extend(m)
        # print(maxHeap)
        heapify(maxHeap)
        # print(maxHeap)
        for i in range(k-1):
            heappop(maxHeap)
        return (maxHeap[0])