class Solution:
    def countVowels(self, word: str) -> int:
        c, l = 0, len(word)
        d = ('aeiou')

        for i in range(l):
                if word[i] in d:
                    c += (l-i)*(i+1)
        return c