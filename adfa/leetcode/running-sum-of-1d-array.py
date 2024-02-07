class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        ans = []
        for i in range(len(nums)):
            prefix_sum += nums[i]
            nums[i]=prefix_sum
        return nums
