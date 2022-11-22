class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == 1:
            return True
        for r in range(rows):
            for c in range(cols):
                if r+1 < rows and c+1 < cols and matrix[r][c] != matrix[r+1][c+1]:
                    return False
        
        return True