class Solution:
    def maxScore(self, s: str) -> int:
        left = 1 if s[0]=='0' else 0
        right =0
        for i in range(1,len(s)):
            right+=int(s[i])
        print(right,left)
        score = left+right
        for i in range(1,len(s)-1):
            if s[i]=='1':
                right-=1
            else:
                left+=1
            score = max(score, left+right)
        return score