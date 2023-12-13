class Solution:
    def reverseWords(self, s: str) -> str:
        n= len(s)
        splits = s.split()
        splits=splits[::-1]
        ans= " ".join(splits)
        return str(ans)
