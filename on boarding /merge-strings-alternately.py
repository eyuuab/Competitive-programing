class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans =[]
        l,r=0,0
        while l<len(word1) or r<len(word2):
            if l<len(word1):
                ans.append(word1[l])
                l+=1
            if r<len(word2):
                ans.append(word2[r])
                r+=1
        return "".join(ans)
            