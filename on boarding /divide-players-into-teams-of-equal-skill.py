class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        total = sum(skill)
        skill.sort()
        l,r=0,n-1
        equal = skill[0]+skill[r]
        pro = 0
        while r>=l:
            if skill[l] +skill[r] !=equal:
                return -1
            else:
                pro += skill[l] * skill[r]
            l+=1
            r-=1
        return pro
