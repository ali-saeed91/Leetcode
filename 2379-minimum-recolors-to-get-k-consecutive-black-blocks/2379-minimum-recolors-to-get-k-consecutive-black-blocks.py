class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start = 0
        minfreq = float("inf")
        dic = {"W":0, "B":0}
        
        for i in range(0,len(blocks)):
            dic[blocks[i]] +=1
            
            if (i - start + 1) >= k:
                if dic["B"] == k:
                    return 0
                
                minfreq = min(minfreq,dic["W"])
                dic[blocks[start]] -=1
                start +=1
            
        return minfreq
        