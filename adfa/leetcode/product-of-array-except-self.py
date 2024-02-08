class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,sufix = [nums[0]],[nums[-1]]

        for i in range(1,len(nums)):
            prefix.append(prefix[-1]*nums[i])
     
        for i in range(len(nums)-2,-1,-1):
            sufix.append(sufix[-1]*nums[i])
        sufix = sufix[::-1]
      
        for i in range(len(nums)):
            val = prefix[i-1] if i!=0 else 1
            val *= sufix[i+1] if i!=len(nums)-1 else 1
            nums[i] = val
        return nums