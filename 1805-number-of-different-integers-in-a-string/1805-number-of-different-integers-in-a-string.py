class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = re.sub("[a-z]+"," ",word)
        s = s.split()
        for i in range(len(s)):
            s[i] = int(s[i])
        s= set(s)
        return len(s)