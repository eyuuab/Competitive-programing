class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s)==1:
            
            return ""
        if s[0]!='a':
            return 'a'+s[1:len(s)]
        l,r =0,len(s)-1
        while r>l:
            if s[l]!='a':
                return s[0:l]+ 'a'+ s[l+1:len(s)]

            l+=1
            r-=1
        return s[0:len(s)-1]+'b'
                
