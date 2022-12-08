class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]
        for ch in s:
            for i in range(len(output)):
                if ch.isalpha():
                    output.append(output[i]+ch.lower())
                    output[i] = output[i]+ch.upper()
                else:
                    output[i] = output[i]+ch
        return output