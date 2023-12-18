class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        tracker=defaultdict(int)

        for i in cpdomains:
            m=i.split()
            num=int(m[0])
            
            n=len(m[1])
            for j in range(n-1,-1,-1):
                if m[1][j] =='.':
                    tracker[m[1][j+1:]]+=num
            tracker[m[1]]+=num
        ans=[]
        for i in tracker.keys():
            temp=str(tracker[i])+" "+ i
            ans.append(temp)
        return ans

                




        
        
        