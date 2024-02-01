class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r=0,len(s1)-1
        ms1 = defaultdict(int)
        ms2 = defaultdict(int)

        for i in s1:
            ms1[i]+=1
        for i in range(len(s1)):
            if i < len(s2):
                ms2[s2[i]]+=1
        while r<len(s2):
            if ms1==ms2:
                return True
            ms2[s2[l]]-=1
            if ms2[s2[l]]==0:
                del ms2[s2[l]]
            l += 1
            r += 1
            if r<len(s2):
                ms2[s2[r]]+=1
        return False