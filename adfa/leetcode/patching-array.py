class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cnt = rng = 0
        nums = nums[::-1]
        i = 1
        rng = 0
        while rng<n:
            while nums and nums[-1]<=i:
                rng +=nums.pop()
                i = rng
            if i>rng:
                rng+=i
                i=rng
                cnt+=1
            i+=1
        return cnt

                