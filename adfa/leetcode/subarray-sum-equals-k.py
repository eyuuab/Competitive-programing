class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp  = defaultdict(int)
        mp[0]+=1
        prefix_sum = cnt = 0
        for i in range(len(nums)):
            prefix_sum +=nums[i]
            if prefix_sum-k in mp:
                cnt+=mp[prefix_sum-k]
            mp[prefix_sum]+=1
        return cnt
