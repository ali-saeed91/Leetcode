class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        
        def BackTracking(CurString,openC,closeC):
            if len(CurString)==2*n:#append string when its length is 2*n
                res.append(CurString)
                return
            #append open bracket when its count less than n
            if openC<n:
                BackTracking(CurString+"(",openC+1,closeC)
            #append closing bracket to the string when its count less than n and its 
            #count less than the count of opening brackets.
            if closeC<n and openC>closeC:
                BackTracking(CurString+")",openC,closeC+1)
        
        BackTracking("",0,0)
        
        return res