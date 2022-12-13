class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        arr = s.split()
        # print(arr)
        if len(pattern) != len(arr):
            return False
        if len(set(arr)) != len((set(pattern))):
            return False
        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = pattern[i]
            else:
                if dic[arr[i]] != pattern[i]:
                    return False
        return True