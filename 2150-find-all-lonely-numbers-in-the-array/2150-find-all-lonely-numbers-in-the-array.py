class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        arr = []
        dic = Counter(nums)
        for k,v in dic.items():
            if v == 1 and k-1 not in dic and k+1 not in dic:
                arr.append(k)
        return arr