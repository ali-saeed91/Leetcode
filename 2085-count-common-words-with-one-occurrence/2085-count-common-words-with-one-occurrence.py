class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        s1= list(set(words1))
        set2 = list(set(words2))
        # print(s1)
        # print(set2)
        for string in s1:
            if words1.count(string) == 1 and words2.count(string) == 1:
                count +=1
        return (count)