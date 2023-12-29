class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #bubble sort algorithm
        for i in range(len(nums)):
            for j in range(0,len(nums)-i-1):
                s1 = str(nums[j])+str(nums[j+1])
                s2 = str(nums[j+1])+str(nums[j])
                if s1<s2:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        if set(nums)=={0}:
            return "0"
        return "".join(map(str,nums))

