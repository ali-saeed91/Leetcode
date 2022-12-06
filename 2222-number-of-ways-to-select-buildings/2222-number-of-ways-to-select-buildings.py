class Solution:
    def numberOfWays(self, s: str) -> int:
        c1 = 0
        c0 = 0
        c10 = 0
        c01 = 0
        c010 = 0
        c101 = 0
        for i in range(len(s)):
            if s[i] == '0':
                c010 += c01
                c10 += c1
                c0 += 1
            else:
                c101 += c10
                c01 += c0
                c1 += 1
        return c010 + c101
            