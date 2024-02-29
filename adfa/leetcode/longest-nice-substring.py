class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        counter = Counter(s)
        for char in range(len(s)):
            if s[char].lower() not in counter or s[char].upper() not in counter:
                left = self.longestNiceSubstring(s[:char])
                right = self.longestNiceSubstring(s[char+1:])
                return max(left, right, key = len)
        return s