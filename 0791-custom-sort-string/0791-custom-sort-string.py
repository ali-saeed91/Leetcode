class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        # print(count)
        arr = []
        for o in order:
            if count[o] > 0:
                arr.append(count[o]*o)
                count.pop(o)
        # print(arr)
        # print(count)
        for k,v in count.items():
            arr.append(k*v)
        return ''.join(arr)
            
            