class Solution:
    def numberOfMatches(self, n: int) -> int:
        matchs = 0
        temp=n
        while n>1:
            if n%2==0:
                matchs+=n//2
                n=n//2
            else:
                matchs+=(n-1)//2
                n= (n-1)//2 +1
        return matchs