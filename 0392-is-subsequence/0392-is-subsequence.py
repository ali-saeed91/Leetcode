class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "" and len(t) > 0:
            return True
        if len(s) > 0 and t == "":
            return False
        idx = [] 
        for i in range(0,len(s)):
            if s[i] not in t:
                return False
            if t.count(s[i]) < s.count(s[i]):
                return False
            cidx = t.index(s[i])
            if len(idx) > 0  and t.count(s[i]) == 1 and cidx <= idx[-1]:
                return False
            idx.append(cidx)
            s.replace(s[i],"")
            if idx.count(i) > 1:
                return False
            
        print(idx)
        return True