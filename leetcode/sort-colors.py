class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        my=[]
        size=len(nums)
        for i in range(size):
            for j in range(i+1,size):
                if nums[i]>nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                    my.append(nums[j])
        return my
        
