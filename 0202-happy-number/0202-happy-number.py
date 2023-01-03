class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n not in s:
            s.add(n)
            new=0
            for i in str(n):
                new +=int(i)**2
            if new == 1:
                return True
            n=new
        return False