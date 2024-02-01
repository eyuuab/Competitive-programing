class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l, r = 0, 0
        maxl = 0
        max_freq = 0
        mp = defaultdict(int)

        while r < len(answerKey):
            mp[answerKey[r]] += 1
            max_freq = max(max_freq, mp[answerKey[r]])
            if (r - l +   1) - max_freq > k:
                mp[answerKey[l]] -= 1
                l += 1

            maxl = max(maxl, r - l + 1)
            r += 1

        return maxl
        