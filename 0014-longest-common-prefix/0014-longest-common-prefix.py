class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs[0] == "":
            return ""
        base = strs[0]
        # print(base)
        if len(strs) == 1:
            return base
        for string in strs:
            for i in range(0, len(base)):
                if i >= len(string) or base[i] != string[i]:
                    base = base[0:i]
                    break
        return base