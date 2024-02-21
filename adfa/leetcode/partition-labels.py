class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        for i in range(len(s)):
            mp[s[i]]=i
        ans = []
        prev = -1
        maxl=0
        for i in range(len(s)):
            maxl = max(maxl,mp[s[i]])
            if maxl==i:
                ans.append(maxl-prev)
                prev = maxl
        return ans