from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(idx, subset):
            if len(subset) == n:
                ans.append(subset[:])
                return
            ans.append(subset[:])
            for i in range(idx, n):
                subset.append(nums[i])
                
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return ans