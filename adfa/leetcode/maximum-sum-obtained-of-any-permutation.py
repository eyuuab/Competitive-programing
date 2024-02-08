class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0 for i in range(len(nums)+1)]
        for start,end in requests:
            prefix[start]+=1
            prefix[end+1]-=1
        prefix=list(accumulate(prefix))
        prefix.sort(reverse = True)
        nums.sort(reverse = True)
        r = ans = 0
        while r<len(prefix):
            if prefix[r]==0:
                break
            ans+=prefix[r]*nums[r]
            r+=1
        return ans%(10**9 + 7)