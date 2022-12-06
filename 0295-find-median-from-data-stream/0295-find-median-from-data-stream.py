class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.minHeap, num)
        heappush(self.maxHeap, -heappop(self.minHeap))
       
        if len(self.maxHeap) > len(self.minHeap) +1:
            heappush(self.minHeap, -heappop(self.maxHeap))
     
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0]/2 + self.minHeap[0]/2)
        return -self.maxHeap[0]/1.0
        