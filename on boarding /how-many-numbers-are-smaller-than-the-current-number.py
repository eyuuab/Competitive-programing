class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        ans = []
        mp = defaultdict(int)
        for i in range(len(nums)):
            if temp[i] not in mp:
                mp[temp[i]] = i
        for i in range(len(nums)):
            ans.append(mp[nums[i]])
        return ans   

