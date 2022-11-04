class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        out = []
        (x1,y1) = (0,0)
        for x,y in points:
            distance = math.sqrt(((x-x1)**2) + ((y-y1)**2))
            maxHeap.append([distance,x,y])
        heapify(maxHeap)
        while k > 0:
            _,i,j = heappop(maxHeap)
            out.append([i,j])
            k -=1
        return out