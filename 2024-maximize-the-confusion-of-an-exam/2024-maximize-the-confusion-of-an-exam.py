class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxFreq=0
        dic= {'T':0, 'F':0}
        j=0
        for i in range(len(answerKey)):
            dic[answerKey[i]] +=1
            
            while dic['T'] > k and dic['F'] > k:
                dic[answerKey[j]] -=1
                j +=1
                
            maxFreq=max(maxFreq,i-j+1)
        return (maxFreq)