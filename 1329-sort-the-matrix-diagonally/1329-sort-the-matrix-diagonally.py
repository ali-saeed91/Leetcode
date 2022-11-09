class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        temp = defaultdict(list)
        res = mat[:][:]
        # print(res)
        for i in range(0,m):
            for j in range(0,n):
                temp[i-j].append(mat[i][j])
        # print(temp)
        for key, value in temp.items():
            value.sort(reverse = True)
        # print(temp)
        for i in range(0,m):
            for j in range(0,n):
                res[i][j] = temp[i-j].pop()
        return res
        