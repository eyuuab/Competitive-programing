class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefix_sum = 0
        mp = defaultdict(int)
        mp[0] += 1
        l = 0

        for r in range(len(nums)):
            prefix_sum += nums[r] % 2
            if prefix_sum - k in mp:
                cnt += mp[prefix_sum - k]

            mp[prefix_sum] += 1

        return cnt