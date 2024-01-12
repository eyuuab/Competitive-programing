from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        mp = defaultdict(int)
        l, r = 0, 0
        max_len = 0

        for r in range(n):
            mp[fruits[r]]+=1
            while len(mp)>2:
                if mp[fruits[l]] == 1:
                    del mp[fruits[l]]
                else:
                    mp[fruits[l]] -= 1
                l+=1
            max_len = max(max_len , r-l+1)
        return max_len
            


        return max_len
