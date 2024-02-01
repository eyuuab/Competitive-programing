class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = cnt = 0
        l,r = 0,0
        while r<len(nums) and l<=r:
            if nums[r]==0:
                cnt+=1
            while cnt>1:
                if nums[l]==0:
                    cnt-=1
                l+=1
            max_len = max(max_len,r-l+1)
            r+=1
        return len(nums)-1 if max_len==len(nums) else max_len-cnt