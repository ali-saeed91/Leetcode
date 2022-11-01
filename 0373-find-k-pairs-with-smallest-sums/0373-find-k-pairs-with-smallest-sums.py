class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []
        
        heap = []
        for i in range(len(nums1)):                                  
            heappush(heap, (nums1[i] + nums2[0], i, 0))           #Step 1
            
        result = []
        while heap and k > 0:                                     
            _, i, j = heappop(heap)                         #Step 2
            result.append([nums1[i],nums2[j]])                          #Step 3
            
            if j+1 < len(nums2):                                     #Step 4
                heappush(heap, (nums1[i]+nums2[j+1],i, j+1))      #Step 5
            k-=1
        return result
