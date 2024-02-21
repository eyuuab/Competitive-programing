class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        stack=[]
        max_ = float('inf')
        for i in range(len(nums)):
            max_ = max(max_, nums[i])
            while stack and nums[i]>stack[-1][0]:
                temp = stack.pop()
                ans[temp[1]] = nums[i]
            stack.append((nums[i], i))
       
        print(stack)
        for i in range(len(nums)):
            while stack and nums[i]>stack[-1][0]:
                temp = stack.pop()
                ans[temp[1]]= nums[i]

        return ans
