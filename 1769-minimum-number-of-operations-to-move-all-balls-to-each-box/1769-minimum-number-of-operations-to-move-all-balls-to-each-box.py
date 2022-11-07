class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * len(boxes)
        dis = 0
        for i in range(0,n):
            for j in range(0,n):
                if boxes[j] == "0":
                    continue
                if boxes[j] == "1":
                    dis = (abs(i - j))
                    res[i] += dis
                    # print(res)
        return (res)
                