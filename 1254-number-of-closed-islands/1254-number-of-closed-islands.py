class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def searchClosedIsland(grid, i, j):
            nonlocal K
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j]!=0:
                return

            if i == 0 or j ==0 or i == m-1 or j == n-1 :
                K = False
            grid[i][j] = 1
            searchClosedIsland(grid, i+1, j)
            searchClosedIsland(grid, i-1, j)
            searchClosedIsland(grid, i, j+1)
            searchClosedIsland(grid, i, j-1)
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        K = True
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    K = True
                    searchClosedIsland(grid, i, j)
                    if K == True:
                        count +=1
                    
        return count