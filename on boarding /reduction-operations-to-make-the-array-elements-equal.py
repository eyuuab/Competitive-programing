from typing import List
from collections import defaultdict

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        nums.sort(reverse=True)

        for i in range(len(nums)):
            mp[nums[i]] += 1

        cnt, temp = 0, 1

        for key, val in mp.items():
            mins = len(mp) - temp
            if mins == 0:
                break
            cnt += mins * val
            temp += 1

        return cnt
