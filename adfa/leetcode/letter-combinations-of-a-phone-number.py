class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = []
        
        def backtrack(com, i):
            if len(com)==len(digits):
                ans.append(com)
                return 
            for char in phone[digits[i]]:
                backtrack(com+char, i+1)

        backtrack("", 0)
        return ans