class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        
        for i in range(len(self.mat)):
          
            for j in range(len(self.mat[0])):
                
                if i==0 and j==0:
                    continue
                if i ==0 and j!=0:
                    self.mat[0][j]=self.mat[0][j]+self.mat[0][j-1]
                elif j==0 and i!=0:
                    self.mat[i][0]=self.mat[i][0]+self.mat[i-1][0]
                else:
                    self.mat[i][j] = self.mat[i][j]+self.mat[i-1][j]+self.mat[i][j-1]-self.mat[i-1][j-1]
        print(self.mat)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        val = self.mat[row2][col1-1] if col1!=0 else 0
        val+= self.mat[row1-1][col2] if row1!=0 else 0
        val-= self.mat[row1-1][col1-1] if col1!=0 and row1!=0 else 0 
        return self.mat[row2][col2]- val

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)