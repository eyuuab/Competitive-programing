class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        l,r = 0,0
        max_len = 0
        while r<len(s):
            mp[s[r]]+=1
            while len(mp)<r-l+1:
                mp[s[l]]-=1
                if mp[s[l]]==0:
                    del mp[s[l]]
                l+=1
            max_len = max(max_len, r-l+1)
            r+=1
        return max_len
