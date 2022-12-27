class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def recursive(arr, word):
            if not word:
                res.append(arr)
                return
            for i in range(1,len(word)+1):
                curr = word[:i]

                if curr == curr[::-1]:
                    recursive(arr + [curr], word[i:])
        recursive([],s)
        return res