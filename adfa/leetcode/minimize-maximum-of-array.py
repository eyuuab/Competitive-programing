class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_ = nums[0]
        cur_sum = nums[0]
        for i in range(1,len(nums)):
            cur_sum += nums[i]
            avg = math.ceil(cur_sum/(i+1))
            max_ = max(max_, avg)
        return max_