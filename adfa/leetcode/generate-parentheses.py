class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(open, close , com):
            if len(com) == 2*n:
                ans.append(com)
                return 
            if open<n:
                backtrack(open+1, close, com+'(')
            if close< open:
                backtrack(open, close+1, com+')')
        backtrack(0,0,'')
        return ans