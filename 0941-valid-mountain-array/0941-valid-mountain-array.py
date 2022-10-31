class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3 or arr[0]>=arr[1] or arr[len(arr)-1] > arr[len(arr)-2]:
            return False
        start = 0
        end = len(arr) -1
        midval = max(arr)
        mid = arr.index(midval)
        while start != mid:
            if arr[start] >= arr[start+1]:
                return False
            start +=1
        while mid != end:
            if arr[mid] <= arr[mid+1]:
                return False
            mid +=1
        return True
                
                