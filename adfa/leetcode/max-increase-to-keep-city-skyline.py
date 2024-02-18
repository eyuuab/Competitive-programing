class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = [0]*n
        col = [0]*n
        ans = 0
        for i in range(n):
            for j in range(n):
                row[i] = max(row[i],grid[i][j])
                col[j] = max(col[j],grid[i][j])
        for i in range(n):
            for j in range(n):
                ans += min(row[i],col[j])-grid[i][j]
        return ans
        