class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        # print(arr)
        maps= {}
        if len(arr) != len(pattern):
            return False
        p = Counter(pattern)
        st = Counter(arr)
        # print(p)
        # print(st)
        set1 = set(p)
        set2 = set(st)
        if len(set1) != len(set2):
            return False
        
        # print(set1)
        # print(set2)
        for i in range(len(arr)):
            if arr[i] not in maps:
                maps[arr[i]] = pattern[i]  
            elif maps[arr[i]] != pattern[i]:
                return False
        return True
    