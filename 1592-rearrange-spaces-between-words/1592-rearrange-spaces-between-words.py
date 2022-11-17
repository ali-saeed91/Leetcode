class Solution:
    def reorderSpaces(self, text: str) -> str:
        totalsp = text.count(" ")
        print(totalsp)
        wordarr = text.split()
        print(wordarr)
        ln = len(wordarr)
        # print(ln)
        out =""
        diff = 0 if ln == 1 else totalsp // (ln-1)
        addif = totalsp - diff * (ln -1)
       
        out = (' ' * diff).join(wordarr) + (' ' * addif)
    
        return out