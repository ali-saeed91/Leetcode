class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = Counter(arr)
        # print(s)
        count = []
        for k, v in s.items():
            count.append(v)
        # print(count)
        rev =sorted(count)
        print(rev)
        slist = list(set(count))
        # print(slist)
        slist.sort()
        # print(slist)
        if rev == slist:
            return True
        return False