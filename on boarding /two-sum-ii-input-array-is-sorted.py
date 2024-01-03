class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l,r =0,n-1
        while r >l:
            cur_sum = nums[r]+nums[l]
            if cur_sum>target:
                r-=1
            elif cur_sum<target:
                l+=1
            else:
                return [l+1,r+1]

