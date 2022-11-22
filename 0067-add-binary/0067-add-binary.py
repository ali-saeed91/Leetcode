class Solution:
    def addBinary(self, a: str, b: str) -> str:
        adecimal=(int(a,base=2))
        bdecimal=(int(b,base=2))
        c =adecimal+bdecimal
        # print(c)
        binc=(bin(c))
        binc = binc[2:]
        return binc
       