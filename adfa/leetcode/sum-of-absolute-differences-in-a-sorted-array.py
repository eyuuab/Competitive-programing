class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix=[0]+[nums[0]]
        postfix=[0]+[nums[-1]]
        total = sum(nums)
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
        for i in range(len(nums)-2,-1,-1):
            postfix.append(postfix[-1]+nums[i])
        postfix=postfix[::-1]
        print(prefix,postfix)
        ans=[]
        res=0
        for i in range(len(nums)):
            res = nums[i]*i - prefix[i] if i!=0 else 0
            res+= postfix[i+1] - nums[i]*(len(nums)-i-1)
            ans.append(res)
            
        return ans