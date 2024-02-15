class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp ={}
        for char in s:
            mp[char] = mp.get(char, 0)+1
          
        cnt = 0
        lgz = 0
       
        for key, val in mp.items():
            if val%2==0:
                cnt+=val
                lgz+=1
            else:
                cnt+=val-1
        if len(mp)==lgz:
            return cnt
        else:
            return cnt+1