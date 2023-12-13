class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        map_nums = defaultdict(int)
        for i in range(len(nums)):
            map_nums[nums[i]] = i
        for ops in operations:
            idx = map_nums[ops[0]]
            map_nums[ops[1]] = idx
            del map_nums[ops[0]]
        for key, value in map_nums.items():
            nums[value] = key
        return nums