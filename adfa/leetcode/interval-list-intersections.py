class Solution:
    def intervalIntersection(self, flist: List[List[int]], slist: List[List[int]]) -> List[List[int]]:
        ans = []
        r=0
        for num in flist:
            start = num[0]
            end = num[1]
            temp=[]

            while r<len(slist) and end>=slist[r][0]:
                temp.append(max(start,slist[r][0])) 
                temp.append(min(end,slist[r][1]))
                r+=1
                if temp[0]<=temp[1]:
                    ans.append(temp)
                temp=[]
            if r>0:
                r-=1
            # if r>0 and start==slist[r-1][1]:
            #     ans.append([start],slist[r-1][1])
            # elif r>0 and end == slist[r-1][1]:
            #     ans.append([end, slist[r-1][1]])
        return ans
