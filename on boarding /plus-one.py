class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        last = digits[-1]
        if last<9:
            digits[n-1] = last+1
            return digits
        else:
            num = int("".join(map(str, digits)))
            num+=1
            digit_list = [int(digit) for digit in str(num)]
            return digit_list