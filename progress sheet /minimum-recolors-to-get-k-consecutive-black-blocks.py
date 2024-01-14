class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ans = float('inf')
        for i in range(n - k + 1):
            window = blocks[i:i + k]
            cnt = window.count('W')
            ans = min(ans, cnt)
        return ans