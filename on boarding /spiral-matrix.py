class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        ans  = []
        m,n = len(mat), len(mat[0])
        k,l=0,0
        last_r, last_c = m-1,n-1
        while k<=last_r and l<=last_c:
            for i in range(l,last_c+1):
                ans.append(mat[k][i])
            k+=1
            for i in range(k,last_r+1):
                ans.append(mat[i][last_c])
            last_c-=1
            if k<=last_r:
                for i in range(last_c, l - 1, -1):
                    ans.append(mat[last_r][i])
                last_r-=1
            if l<=last_c:
                for i in range(last_r,k-1,-1):
                    ans.append(mat[i][l])
                l+=1
        return ans
        

            
