class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alpha = [c for c in s if c.isalpha()]
        alpha.reverse()
        result = list(s)
        idx = 0
        for i in range(len(s)):
            if result[i].isalpha():
                result[i] = alpha[idx] 
                idx+=1
        return ''.join(result)