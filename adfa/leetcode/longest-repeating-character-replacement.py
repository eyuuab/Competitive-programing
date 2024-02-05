class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_len = 0
        max_freq = 0
        mp = defaultdict(int)

        while r < len(s):
            mp[s[r]] += 1
            max_freq = max(max_freq, mp[s[r]])
            if (r - l + 1) - max_freq > k:
                mp[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len