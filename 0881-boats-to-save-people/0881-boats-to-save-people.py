class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True) # ([3,2,2,1])
        i=0 #i=0,1,2,3
        j=len(people)-1 #j=3,2,2
        while i<=j: #0<=3,1<=3,2<=2,
            if people[i] + people[j] <=limit: # 3+1 <= 3,2+1<=3, 2
                j -=1 #j=2
            i +=1 #i=1,2,3
        return i