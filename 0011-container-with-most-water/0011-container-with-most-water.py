class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        maxVol =0
        
        while left < right:
            # area = width * height
            lh = height[left]
            rh = height[right]
            
            vol = min(lh,rh) * (right-left)
            
            if vol > maxVol:
                maxVol = vol
            if lh >= rh:
                while left < right and height[right] <= rh:
                    right -=1
            else:
                while left < right and height[left] <= lh:
                    left +=1
        return maxVol
            
            