from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        diff = 0
        D1 = datetime.strptime(date1, '%Y-%m-%d').date()
        # print(D1)
        D2 = datetime.strptime(date2, '%Y-%m-%d').date()
        # print(D2)
        diff = abs(D2-D1).days
        return diff