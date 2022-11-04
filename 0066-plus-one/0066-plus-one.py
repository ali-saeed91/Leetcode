class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        out = ""
        fin = []
        for i in range(0,len(digits)):
            digits[i] = str(digits[i])
        # print(digits)
        s = "".join(digits)
        # print(s)
        num = int(s)
        # print(num)
        num +=1
        snum = str(num)
        # print("strnum",snum)
        for j in range(0,len(snum)-1):
            out += snum[j] + ","
        # print(out)
        out += snum[len(snum)-1]
        # print(out)
        for char in out:
            if char.isdigit():
                fin.append(int(char))
        return (fin)