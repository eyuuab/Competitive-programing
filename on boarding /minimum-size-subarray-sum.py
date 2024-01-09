class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n= len(nums)
        prefix, min_len = 0,float('inf')
        l=0
        for i in range(n):
            prefix+=nums[i]
            while prefix>=target:
                prefix-=nums[l]
                min_len = min(min_len, i-l+1)
                l+=1
        return 0 if min_len ==float('inf') else min_len

