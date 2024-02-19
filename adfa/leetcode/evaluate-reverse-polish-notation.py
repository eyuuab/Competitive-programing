class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            if char not in ["+", "-", "*", "/"]:
                stack.append(char)
            else:
                t,s = int(stack.pop()), int(stack.pop())
                opnt = char
                if opnt=='+':
                    stack.append(s+t)
                elif opnt=='-':
                    stack.append(s-t)
                elif opnt=='*':
                    stack.append(s*t)
                else:
                    stack.append(int(s/t))
            
        return int(stack.pop())




                
