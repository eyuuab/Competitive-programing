class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num]+=1
        mp = defaultdict(int)
        l=r= 0
        cnt=0
       
        while r<len(nums):
            mp[nums[r]]+=1
            if len(mp)==len(counter):
                cnt+=1

            while mp[nums[l]]>1 and len(mp)==len(counter):
                mp[nums[l]]-=1
                l+=1
                cnt+=len(nums)-r
            r+=1
        return cnt
                


