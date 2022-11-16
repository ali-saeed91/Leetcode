class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        misArr =[]
        count = 0
        maxNum = max(arr)
        for i in range(1,maxNum+k+1):
            # print(i)
            if i not in arr:
                misArr.append(i)
                count +=1
        return misArr[k-1]