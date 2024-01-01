class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        if num<0:
            num= num*-1
            x = list(str(num))
            x.sort(reverse=True)
            x=''.join(map(str,x))
            return int(x)*-1
        else:
            x =list(str(num))
            x.sort()
            i=0
            while i<len(x):
                if int(x[i])==0:
                    i+=1
                else:
                    x[0],x[i]=x[i],x[0]
                    break
            x=''.join(map(str,x))
            return int(x)



        