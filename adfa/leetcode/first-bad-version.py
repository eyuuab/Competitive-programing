# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left , right = 1, n
        while left <= right :
            mid = right - (right-left)//2
            res = isBadVersion(mid)
            if res == False:
                left = mid +1
            else:
                right = mid -1
        # print(left, right)
        return left