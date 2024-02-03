class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        l,r = 0,len(nums)-k
        total= sum(nums)
        min_sum = cur_sum =sum(nums[l:r])
        if k==len(nums):
            return total
        while r<len(nums):
            cur_sum +=nums[r]
            cur_sum-=nums[l]
            min_sum = min(cur_sum,min_sum)
            r+=1
            l+=1
        return total-min_sum