class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        points = cardPoints[len(cardPoints)-k:] + cardPoints[:k]
        curSum = sum(points[:k])
        maxSum = curSum
        
        for i in range(len(points)-k):
            curSum -= points[i] - points[i-k]
            maxSum = max(maxSum, curSum)
        # print(maxSum)
        return(maxSum)
            