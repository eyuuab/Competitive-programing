class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        ans = []
        for i in range(len(nums)):
            if counter[nums[i]]>len(nums)/3 and nums[i] not in ans:
                ans.append(nums[i])
        return ans