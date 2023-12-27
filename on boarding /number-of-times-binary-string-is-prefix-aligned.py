class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        cnt , ones =0,0 
        maxn =0      
        for i in range(len(flips)):
            ones+=1
            maxn = max(maxn, flips[i]) 
            if maxn==ones:
                cnt+=1
        return cnt
            
