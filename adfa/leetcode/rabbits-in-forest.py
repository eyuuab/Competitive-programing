class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mp = defaultdict(int)
        for ans in answers:
            mp[ans]+=1
        res = 0
        for key, val in mp.items():
            if key ==0:
                res+=val
            elif key>=val-1:
                res+=key+1
            else:
                while val>0:
                    if key>=val-1:
                        res +=key+1
                        val-=key+1
                    else:
                        res+=key+1
                        val-=key+1

        return res