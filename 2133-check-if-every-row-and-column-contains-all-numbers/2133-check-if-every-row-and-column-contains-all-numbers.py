class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row = defaultdict(set)
        col = defaultdict(set)
        # print(row)
        # print(col)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] in row[i] or matrix[i][j] in col[j]:
                    return False
                row[i].add(matrix[i][j])
                col[j].add(matrix[i][j])
        # print(row)
        # print(col)
        return True