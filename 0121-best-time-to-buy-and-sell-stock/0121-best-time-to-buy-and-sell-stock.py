class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxp = 0
        while right < len(prices):
            curp = prices[right] - prices[left]
            if prices[left] < prices[right]:
                maxp = max(curp, maxp)
            else:
                left = right
            right +=1
        return (maxp)
            