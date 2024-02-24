class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_nums = [float('inf')] * len(nums)

        for i in range(1, len(nums)):
            min_nums[i] = min(min_nums[i - 1], nums[i - 1])

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > min_nums[j]:
                while stack and stack[-1] <= min_nums[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False
