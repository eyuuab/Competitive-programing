class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums),2):
            feq = nums[i]
            val = nums[i+1]
            for j in range(feq):
                ans.append(val)
        return ans