class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans =[]
        ptve=[]
        ntve=[]
        for i in range(len(nums)):
            if nums[i]>0:
                ptve.append(nums[i])
            else:
                ntve.append(nums[i])
        print(ptve,ntve)
        for i in range(len(ptve)):
            ans.append(ptve[i])
            ans.append(ntve[i])
        return ans