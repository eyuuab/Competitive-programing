class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_s = []
        sp=set(spaces)
        for i in range(len(s)):
            if i in sp:
                new_s.append(' ')
            new_s.append(s[i])
        return ''.join(new_s)