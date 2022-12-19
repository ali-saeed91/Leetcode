class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        diff1 = max(event1[0],event2[0])
        # print(diff1)
        diff2 = min(event1[1],event2[1])
        # print(diff2)
        if diff1 <= diff2:
            return True
        return False