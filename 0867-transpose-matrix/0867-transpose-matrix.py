class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = [[None] * rows for r in range(cols)]
        for r in range(rows):
            for c in range(cols):
                ans[c][r] = matrix[r][c]
        return ans