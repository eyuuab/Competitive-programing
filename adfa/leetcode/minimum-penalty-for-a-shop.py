class Solution:
    def bestClosingTime(self, c: str) -> int:
        left,right = 0 , c.count('Y')
        min_sum = left+right
        ans = 0
       
        for i in range(len(c)):
            if c[i]=="Y":
                right-=1
            else:
                left+=1
            if min_sum> left +right:
                min_sum = left+right
                ans = i+1

        
        return ans
        