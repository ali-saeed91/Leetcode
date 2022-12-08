class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        odd = []
        res = []
        out = ""
        for i in str(num):
            i = int(i)
            if i %2 == 0:
                even.append(-i)
                res.append(False)
            else:
                odd.append(-i)
                res.append(True)
                
        heapify(even)
        heapify(odd)
     
        for i in range(len(res)):
            if res[i]:
                res[i] = -heappop(odd)
            else:
                res[i] = -heappop(even)
        for i in range(len(res)):
            res[i] = str(res[i])
            out +=res[i]
        return (int(out))