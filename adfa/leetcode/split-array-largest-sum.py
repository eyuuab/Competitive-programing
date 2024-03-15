class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2
            count = 1
            current_sum = 0

            for num in nums:
                current_sum += num
                if current_sum > mid:
                    count += 1
                    current_sum = num

            if count <= k:
                high = mid
            else:
                low = mid + 1

        return low