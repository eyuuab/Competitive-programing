class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack= []
        optn = 0
        for char in s:
            if stack and char ==')':
                stack.pop()
            elif char=='(':
                stack.append(char)
            elif not stack and char==')':
                optn+=1
        return len(stack)+optn
