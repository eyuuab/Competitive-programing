class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = s.count('0')
        ones = len(s)-zeros
        prefix_one = prefix_zero = 0
        cnt = 0
        for char in s:
            if char == '1':
                cnt+= prefix_zero*(zeros - prefix_zero)
                prefix_one+=1
            else:
                cnt+=prefix_one * (ones- prefix_one)
                prefix_zero+=1
        return cnt