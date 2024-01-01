class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        cnt = 0
        l, r = 0, len(piles) - 1
        while r > l:
            cnt += piles[r - 1]
            r -= 2
            l += 1
        return cnt
