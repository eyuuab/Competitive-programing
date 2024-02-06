from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count, window = defaultdict(int), defaultdict(int)
        if len(t) > len(s):
            return ""
        for char in t:
            count[char] += 1
        ans, flag = '', False
        min_len, l, r = float('inf'), 0, 0
        tl, tr = 0, 0

        while r < len(s):
            window[s[r]] += 1

            while all(window[char] >= count[char] for char in count) and l <= r:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                temp = min_len
                min_len = min(min_len, r - l + 1)
                if temp != min_len:
                    tr = r
                    tl = l
                l += 1
            r += 1
        
        if min_len == float('inf'):
            return ""
        
        return s[tl:tr + 1]