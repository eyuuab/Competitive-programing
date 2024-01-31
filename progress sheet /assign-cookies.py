class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r=0,0
        cnt=0
        g.sort()
        s.sort()
        while l<len(g) and r<len(s):
            if g[l]<=s[r]:
                cnt+=1
                l+=1
                r+=1
            elif g[l]>s[r]:
                r+=1
            else:
                l+=1
        return cnt