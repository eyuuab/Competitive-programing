class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for word in words:
            if set(word.lower())<=set("qwertyuiop" )or set(word.lower())<=set("asdfghjkl") or set(word.lower())<=set("zxcvbnm"):
                ans.append(word)
        return ans