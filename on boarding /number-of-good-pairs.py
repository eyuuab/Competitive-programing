class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt=0
        size=len(nums)
        for i in range(size):
            for j in range(i+1,size):
                if nums[i]==nums[j]:
                    cnt+=1
                 
        return cnt