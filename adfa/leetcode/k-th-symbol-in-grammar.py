class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        def helper(n, k):

            if k==0 or n==0:
                return 0
            prev = helper(n-1, k//2)
            if k%2==0:
                return prev
            if prev==0:
                return 1
            return 0
        return helper(n, k-1)