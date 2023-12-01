class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        cnt = 0
        i = 0

        while i < len(s):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                cnt += roman[s[i + 1]] - roman[s[i]]
                i += 2
            else:
                cnt += roman[s[i]]
                i += 1

        return cnt
            # if s[i] in ["V", "M", "L","D"]:
            #     cnt+=roman[s[i]]
            # else:
            #     if i<len(s)-1 and s[i]=="X" and (s[i+1] =="L" or s[i+1]=="C"):
            #         cnt+=roman[s[i+1]]-10
            #     elif i<len(s)-1 and s[i]=="I" and (s[i+1] =="V" or s[i+1]=="X"):
            #         cnt+=roman[s[i+1]]-1
            #     elif i<len(s)-1 and s[i]=="C" and (s[i+1] =="D" or s[i+1]=="M"):
            #         cnt+=roman[s[i+1]]-100
            #     else:
            #         cnt+=roman[s[i]]
        