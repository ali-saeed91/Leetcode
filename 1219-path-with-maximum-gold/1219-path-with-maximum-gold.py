class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  #m = number of rows and n = number of columns
        max_gold = [0] #global variable for result.

        def dfs(row, col, gold):
            if row == m or col == n or row < 0 or col < 0 or grid[row][col] == 0:
                return

            #once the solution is successful with this code, try running after
            #changing #row >= m or col >= n to row == m and col == n. Why is it
            #giving time limit exceeded error? As per the codition, as soon as
            #row or col == to m or n the function should terminate.

            gold += grid[row][col]
            max_gold[0] = max(gold, max_gold[0])
            temp = grid[row][col]
            grid[row][col] = 0

            dfs(row + 1, col, gold)
            dfs(row - 1, col, gold)
            dfs(row, col + 1, gold)
            dfs(row, col - 1, gold)

            grid[row][col] = temp

        for i in range(m):
            for j in range(n):
                dfs(i, j, 0)

        return max_gold[0]