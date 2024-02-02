class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        left = 0
        max_sum = cur_sum = nums[0]
        mp[nums[0]] += 1
        r, l = 1, 0

        while r < len(nums):
            mp[nums[r]] += 1
            cur_sum += nums[r]

            while mp[nums[r]] > 1 and l < r:
                cur_sum -= nums[l]
                mp[nums[l]] -= 1
                l += 1

            max_sum = max(max_sum, cur_sum)
            r += 1

        return max_sum