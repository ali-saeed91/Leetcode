class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        res = []
        for i in range(m):
            for j in range(n):
                res.append(grid[i][j])
                 
        res = deque(res)
        for _ in range(k):
            res.rotate()
            
        for i in range(m):
            for j in range(n):
                    grid[i][j] = res.popleft()
        return (grid)