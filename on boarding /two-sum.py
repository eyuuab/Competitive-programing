class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        lst = []
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    lst.append(i)
                    lst.append(j)
                    return lst

