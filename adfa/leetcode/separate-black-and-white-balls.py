class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = []
        cnt = zero = 0
        
        for i in range(len(s)):
            if s[i]=="1":
                ones.append(i)
                cnt+=1
            else:
                zero+=1
        res = [len(s)-cnt+i for i in range(cnt)]
        print(cnt, ones,res)
        min_no = 0
        for i in range(len(res)):
            min_no+=res[i]-ones[i]
        return min_no