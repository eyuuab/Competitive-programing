class Solution:
    def isHappy(self, n: int) -> bool:
        def solver(n):
            cnt = 0
            while n:
                rem = n%10
                n = n//10
                cnt+=rem**2
            return cnt
        for i in range(70):
            n = solver(n)
            if n==1:
                return True
        
        return False
