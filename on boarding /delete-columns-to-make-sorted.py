class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        lst=[]
        for i in range(1,len(strs)):
            prev = strs[i-1]
            cur = strs[i]
            for j in range(len(cur)):
                if j not in lst:
                    if prev[j] >cur[j]:
                        cnt+=1
                        lst.append(j)
            print(prev, cur)
        return cnt
