class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt, pref = 0,0
        mp = defaultdict(int)
        mp[0]=1
        for i in range(len(nums)):
            pref += nums[i]
            remainder  = pref%k
            if remainder in mp:
                cnt += mp[pref%k]
            mp[remainder] +=1
        return cnt