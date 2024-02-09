class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if p>total:
            return -1
        rem = total%p
        if rem==0:
            return 0
        # # find the minimum subarry sum == to reminder
        min_len = float('inf')
        # prefix =0
        # while r<len(nums):
        #     prefix+=nums[r]
        #     while prefix>rem:
        #         prefix-=nums[l]
        #         l+=1
        #     if prefix==rem:
        #         min_len = min(min_len, r-l+1)
        #     r+=1
        n= len(nums)
        mp = defaultdict(int)
        l,r=0,0
        prefix = 0
        mp[0] = -1
        for i in range(n):
            prefix+=nums[i]
            prefix %= p
            dif = (prefix - rem)%p
            if dif in mp:
                min_len = min(min_len, i-mp[dif])
                
            mp[prefix]=i




        return min_len if min_len<len(nums) else -1
        