class Solution:
    def balancedString(self, s: str) -> int:
        dic = defaultdict(int)
        count = defaultdict(int)
        for char in s:
            dic[char]+=1
            if dic[char] >len(s)//4:
                count[char]+=1
        if len(count)==0:
            return 0
        window = defaultdict(int)
        min_len, l, r = float('inf'), 0, 0
  
        while r < len(s):
            window[s[r]] += 1
            while all(window[char] >= count[char] for char in count) and l <= r:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                min_len = min(min_len, r - l + 1)
                l += 1
            r += 1
                
        return min_len