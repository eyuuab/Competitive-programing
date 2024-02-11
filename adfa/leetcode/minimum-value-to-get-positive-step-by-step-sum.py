class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums))
        min_ = min(prefix)
        if min_ >0:
            return 1
        elif min_<0:
            return min_*-1 +1
        else:
            return 1