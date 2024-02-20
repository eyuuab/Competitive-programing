class Solution:
    
    mp = defaultdict(int)# to make the recoursion fater

    def fib(self, n: int) -> int:
        if n==0:return 0 
        if n==1 or n==2:return 1
        if n in self.mp: return self.mp[n]
        self.mp[n]=self.fib(n-1)+self.fib(n-2)
        return self.mp[n]