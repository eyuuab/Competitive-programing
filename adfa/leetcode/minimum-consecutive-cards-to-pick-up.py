class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mp = defaultdict(int)
        r=1
        mp[cards[0]]=0
        min_len = float('inf')
        while r<len(cards):
            if cards[r] in mp:
                min_len = min( min_len, r - mp[cards[r]] + 1)
            mp[cards[r]]=r
            r+=1
        return -1 if min_len==float('inf') else min_len
            


            