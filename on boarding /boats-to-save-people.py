class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        l,r=0,len(p)-1
        cnt=0
        while r>=l:
            if p[r]+p[l]<=limit:
                cnt+=1
                l+=1
                r-=1
            else:
                cnt+=1
                r-=1
        return  cnt


