class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        cnt = 0
        dup = 0
        for row in range(len(mat)):
            for col in range(len(mat)):
                dup=0
                if row==col:
                    cnt+=mat[row][col]
                    dup+=1
                if col+row ==len(mat)-1:
                    cnt+=mat[row][col]
                    dup+=1
                if dup ==2:
                    cnt-=mat[row][col]
        return cnt