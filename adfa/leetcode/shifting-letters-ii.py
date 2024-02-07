class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0 for i in range(len(s)+1)]
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for l,r,k in shifts:
            shift[l]+=1 if k==1 else -1
            shift[r+1]-=1 if k==1 else -1
        for i in range(1,len(s)):
            shift[i]+=shift[i-1]
        print(shift)
        t = ''
        for i in range(len(s)):
            val = (ord(s[i])-97 +(shift[i]%26))%26
            t+=letters[val]
        return t