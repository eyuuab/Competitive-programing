class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        if nums[low] < nums[high]:
            return nums[low]
        while high > low:
            mid = (high + low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]