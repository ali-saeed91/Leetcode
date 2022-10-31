class Solution:
    def frequencySort(self, s: str) -> str:
        maxHeap = []
        out=""
        s = Counter(s)
        # print(s)
        for num, freq in s.items():
            maxHeap.append([-freq, num])
        heapify(maxHeap)
        # print(maxHeap)
        for i in range(0,len(maxHeap)):
            freq,num = heappop(maxHeap)
            while abs(freq) > 0:
                out += num
                freq +=1
        return (out)