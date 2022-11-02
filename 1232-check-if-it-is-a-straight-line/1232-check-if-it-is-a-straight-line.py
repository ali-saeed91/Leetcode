class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # print(coordinates[0])
        # print(coordinates[:2])
        (x1,y1) , (x2, y2) = coordinates[:2] # slope (y2-y1)/(x2-x1)= m 
        for x, y in coordinates:
            if (x2-x1) * (y-y2) != (x - x2) * (y2 - y1):
                return False
        return True