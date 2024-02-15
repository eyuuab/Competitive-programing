class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            k = nums[i]
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[l]+nums[r]>k:
                    res+=r-l
                    l+=1
                else:
                    r-=1
        return res
                