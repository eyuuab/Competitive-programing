class Solution:
    def largestOddNumber(self, num: str) -> str:

        n=len(num)
        ans = ""
        for i in range(n-1,-1,-1):
            if int(num[i])%2:
                ans+=num[:i+1]
                return ans
        return ans
            