class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans , temp= [], []
        ones = sum(nums)
        zero = 0
        temp.append(ones)
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            if nums[i]:
                ones-=1
            temp.append(zero+ones)
        score = max(temp)
        for i in range(len(temp)):
            if temp[i]==score:
                ans.append(i)
        return ans