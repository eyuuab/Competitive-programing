class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix =0
        n= len(nums)
        rightsum= sum(nums)
        for i in range(n):
            if prefix ==rightsum-nums[i]:
                return i
            prefix+=nums[i]
            rightsum -=nums[i]
        return -1