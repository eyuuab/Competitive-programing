class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        target = nums[-1]
        space = cnt = 0
        for i in range(len(nums)-1, 0, -1):
            
            if target<nums[i-1]:
                space = math.ceil(nums[i-1]/target)
                cnt+=space-1
                target = nums[i-1]//space
            else:
                target = nums[i-1]
            
        return cnt


