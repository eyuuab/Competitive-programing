class Solution:
    def freqAlphabets(self, s: str) -> str:
        n= len(s)
        ans = ""
        i=n-1
        while i>-1:
            if s[i]=="#":
                ans+=chr(ord('a')+(10*(int(s[i-2]))+int(s[i-1]))-1)
                i-=3
            else:
                ans+=chr(ord('a')+int(s[i])-1)
                i-=1
        return ans[::-1]