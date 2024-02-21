class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for idx, val in enumerate(nums):
            nums[idx] = idx+val if val !=0 else 0
        k = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]>=k:
                k = i

        return k==0