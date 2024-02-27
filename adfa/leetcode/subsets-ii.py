class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def helper(idx, com):
            if len(com)==len(nums):
                ans.append(com[:])
                return
            if com not in ans:
                ans.append(com[:])
            for i in range(idx, len(nums)):
                com.append(nums[i])
                helper(i+1, com)
                com.pop()
        helper(0,[])
        return ans