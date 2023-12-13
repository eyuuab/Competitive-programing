class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, lost= [],[]
        for i in matches:
            lost.append(i[1])
            win.append(i[0])
        l=[] #0 lose
        m=[] #1 lose
        c=Counter(lost)
        for i in range(len(win)):
            if c[win[i]]==0:
                l.append(win[i])
            if c[win[i]]==1:
                m.append(win[i])
            if c[lost[i]]==1:
                m.append(lost[i])
        
        l=list(set(l))
        m=list(set(m))
        l.sort()
        m.sort()

        return [l,m]