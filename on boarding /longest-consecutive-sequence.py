class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSeqLen = 0
        while maxSeqLen < len(numSet):
            num = numSet.pop()
            longest = num+1
            while longest in numSet:
                numSet.remove(longest)
                longest += 1
            num = num-1
            while num in numSet:
                numSet.remove(num)
                num -= 1
            maxSeqLen = max(maxSeqLen, longest-num-1)
        return maxSeqLen
            