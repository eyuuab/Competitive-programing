class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0]*len(s)
        i=0
        for idx in indices:
            ans[idx]=s[i]
            i+=1
        return "".join(ans)