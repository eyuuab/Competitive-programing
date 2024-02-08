class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:-x[2])
        ans = [0 for i in range(trips[0][2]+1)]
        for p,start,end in trips:
            if start>0:
                ans[start-1] += p
            else:
                if end-1 != start:
                    ans[start] += p
                else:
                    ans[end]+=p
                    continue
            ans[end-1]-=p
        ans = list(accumulate(ans))
        
        if capacity>=max(ans):
            return True
        else:
            return False