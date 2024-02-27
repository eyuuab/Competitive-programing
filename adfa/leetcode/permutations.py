class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def helper(idx, com):
            if len(com)==len(nums):
                ans.append(com[:])
                return 
            print(com)
            for i in nums:
                if i not in com:
                    com.append(i)
                    helper(i+1,com)
                    com.pop()
        helper(1,[])
        return ans
