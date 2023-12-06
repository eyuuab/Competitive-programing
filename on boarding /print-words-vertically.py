class Solution:
    def printVertically(self, s: str) -> List[str]:
        x=s.split()
        y=max(list(map(len,x)))
        a=[]
        for i in range(y):
            m=''
            for j in range(len(x)):
                if len(x[j])>i:
                    m+=x[j][i]
                else:
                    m+=' '
            for k in range(len(m)):
                m=m.removesuffix(' ')
            a.append(m)
        return a