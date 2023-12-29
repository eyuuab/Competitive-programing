class Solution:
    def sortSentence(self, s: str) -> str:
        lst = list(s.split())
        ans = [0]*len(lst)
        for word in lst:
            idx = int(word[-1])-1
            ln =len(word)
            ans[idx] = word[0:len(word)-1]
        res = " ".join(ans)
        return res
