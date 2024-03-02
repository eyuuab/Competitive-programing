class Solution:
    def solveSudoku(self, grid: List[List[str]]) -> None:
        def solve(i, j):
            if(j == 9):
                i += 1
                j = 0
            if(i == 9): return True
            if(grid[i][j] != "."):
                return solve(i, j+1)
            for dig in range(1, 10):
                if not(dig in row[i] or dig in col[j] or dig in box[(i//3, j//3)]):
                    row[i].add(dig)
                    col[j].add(dig)
                    box[(i//3, j//3)].add(dig)
                    grid[i][j] = str(dig)

                    if(solve(i, j+1)): return 1

                    row[i].remove(dig)
                    col[j].remove(dig)
                    box[(i//3, j//3)].remove(dig)
                    grid[i][j] = "."
            return 0

        box = defaultdict(set)
        row = defaultdict(set)
        col = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if(grid[i][j] != "."):
                    box[(i//3, j//3)].add(int(grid[i][j]))
                    row[i].add(int(grid[i][j]))
                    col[j].add(int(grid[i][j]))
        solve(0, 0)