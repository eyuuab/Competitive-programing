class Solution:
    def minMoves(self, k: int, dbl: int) -> int:
        if dbl==0:
            return k-1
        cnt = 0
        while dbl>0 and k>1:
            if k%2!=0:
                cnt+=1
                k-=1
            else:
                k=k//2
                cnt+=1
                dbl-=1
        return cnt if k==1 else cnt+k-1
                