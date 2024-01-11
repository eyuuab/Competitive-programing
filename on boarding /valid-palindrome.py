class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                t+=char.lower()
        l,r = 0,len(t)-1
        print(t)
        while r>=l:
            if t[l]!=t[r]:
                return False
            l+=1
            r-=1
        return True
"""
        s= s.lower()
        print (s)
        return s == s[::-1]
         for i in s:
            if i != s[size - 1 - s.index(i)]:
                return False
        return True
        """