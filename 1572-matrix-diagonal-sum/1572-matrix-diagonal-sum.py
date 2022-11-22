class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        add = 0
        for r in range(rows):
            for c in range(cols):
                if r == c:
                    add +=(mat[r][c])
                    add +=(mat[-r-1][c])
        if rows % 2 == 1:
            mid = rows//2
            add -= mat[mid][mid]
        return add