class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = n2 = 0
        power = len(num1)-1
        for i in range(len(num1)):
            n1= int(num1[i])*(10**power)+n1
            power-=1
        print(n1)
        power = len(num2)-1
        for i in range(len(num2)):
            n2 =  int(num2[i])*(10**power)+n2
            power-=1
        print(n2)
        return str(n1*n2)
            