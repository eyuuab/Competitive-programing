class Solution:
    def removeElement(self, nums, val: int) -> int:

        idx = 0
        for num in nums:
            if val!=num:
                nums[idx]=num
                idx+=1
        return idx
    
        # l,r=0,1
        # cnt=0
        # if len(nums)==1 and val!=nums[0]:
        #     return 1
        # elif  len(nums)==1 and val==nums[0]:
        #     return 0 
        # while r<len(nums):
        #     if nums[r]!=val and nums[l]==val:
        #         nums[r], nums[l] = nums[l], nums[r]
        #         l+=1
        #         cnt+=1
        #     elif nums[l]!=val:
        #         l+=1
        #     r+=1
        # print(nums)
        # return l


