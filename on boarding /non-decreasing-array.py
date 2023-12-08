class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        ct=0

        for i in range(1,len(nums)):

            if nums[i-1]>nums[i]:
                ct+=1
                if ct>1: return False

                if i >=2 and nums[i]<nums[i-2]:
                    nums[i]=nums[i-1]
        
        return True
        # for i in range(len(nums)-1):
        #     temp = nums
        #     if temp[i]>temp[i+1]:
        #         temp[i+1]=temp[i]
        #         if temp==sorted(temp):
        #             return True
        #         temp2=nums
        #         temp2[i]=temp2[i+1]
        #         if temp2==sorted(temp2):
        #             return True
        #         else:
        #             return False
                
        # return False

       