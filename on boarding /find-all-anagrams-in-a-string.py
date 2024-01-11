
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, len(p) - 1
        ans = []
        mp = defaultdict(int)
        ms = defaultdict(int)

        # Create the frequency count for string p
        for a in p:
            mp[a] += 1

        # Initialize the frequency count for the first window in s
        for i in range(len(p)):
            if i < len(s):
                ms[s[i]] += 1

        while r < len(s):
            if mp == ms:
                ans.append(l)

            # Update the frequency count for the moving window
            ms[s[l]] -= 1
            if ms[s[l]] == 0:
                del ms[s[l]]

            l += 1
            r += 1

            if r < len(s):
                ms[s[r]] += 1

        return ans
