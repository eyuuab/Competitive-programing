class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix =[0]+list(accumulate(nums))
        counter= Counter()
        cnt = 0
        for i in range(len(prefix)):
            if prefix[i]-goal in counter:
                cnt+=counter[prefix[i]-goal]
            counter[prefix[i]]+=1
        return cnt