class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        arr = []
        count = 0
        for i in queries:
            x1 = i[0]
            y1 = i[1]
            r = i[2]
            for j in points:
                x2 = j[0]
                y2 = j[1]
                
                if math.sqrt(((x2-x1)**2) + ((y2-y1)**2)) <= r:
                    count +=1
                    # print(count)        
            arr.append(count)
            count =0
        return arr