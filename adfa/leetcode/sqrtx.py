class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==1 or x==0:
            return x
        low , high = 1, x
        while low <= high:
            mid = low + (high - low)//2
            if mid ** 2 > x:
                high = mid-1
            elif mid **2 < x :
                low = mid +1                
            else:
                return mid
        return high

