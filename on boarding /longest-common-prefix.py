class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        temp = strs[0]
        for i in range(len(temp)):
            for word in strs[1:]:
                if i==len(word) or word[i]!=temp[i]:
                    return temp[0:i]
        return temp