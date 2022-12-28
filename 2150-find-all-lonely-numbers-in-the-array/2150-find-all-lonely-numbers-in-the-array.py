class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        arr = []
        dic = Counter(nums)
        for i in dic:
            if dic[i] == 1 and i-1 not in dic and i+1 not in dic:
                arr.append(i)
        return arr