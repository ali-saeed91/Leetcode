class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        idx=[]
        val=[]
        if s1 == s2:
            return True
     
        for i in range(len(s1)):
            if s1.count(s1[i]) != s2.count(s1[i]):
                return False
            
            if s1[i] != s2[i]:
                idx.append(i)
                val.append(s2[i])
       
        if len(val) == 2:
            return True
        return False
        
        