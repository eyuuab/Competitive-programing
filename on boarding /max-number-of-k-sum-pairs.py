class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r=0,len(nums)-1
        cnt = 0
        while r>l:
            val = nums[r]+nums[l]
            if val ==k:
                cnt+=1
                r-=1
                l+=1
            elif val>k:
                r-=1
            else:
                l+=1
            print(val)
        return cnt