class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        l1 = len(s1)
        
        c2 = Counter()
        
        for i in range(len(s2)):
            if i < l1:
                c2[ s2[i] ] += 1
            else:
                c2[ s2[i - l1] ] -= 1
                c2[ s2[i] ] += 1
            
            if c1 == c2:
                return True
        
        return False