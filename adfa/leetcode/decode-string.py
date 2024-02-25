class Solution:
    def decodeString(self, s: str) -> str:

        stack=[]
        for c in s:
            if c!=']':
                stack.append(c)
            else:
                temp = ''
                while stack and stack[-1]!='[':
                    temp = stack.pop()+temp
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                num = int(num)
                for i in range(int(num)):
                    stack.append(temp)
        return ''.join(stack)
                

    
        