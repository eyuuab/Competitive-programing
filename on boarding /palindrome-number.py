class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x<0:
        #     return False
        y = str(x)
        z = y[::-1]
        if y==z:
            return True
        return False