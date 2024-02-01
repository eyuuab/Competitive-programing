class Solution:
    def maxVowels(self, s: str, k: int) -> int:
      
        vowel=['a','e','i','o','u']
        cnt = v =0
        l,r = 0,k

        for i in range(k):
            if s[i] in vowel:
                cnt+=1
        v=cnt
        while r<len(s):
            if s[r] in vowel:
                cnt+=1
            if s[l] in vowel:
                cnt-=1
            v = max(v,cnt)
            l+=1
            r+=1
        return v