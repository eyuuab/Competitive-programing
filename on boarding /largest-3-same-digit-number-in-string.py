class Solution:
    def largestGoodInteger(self, num: str) -> str:

        l,r=0,2
        largest = ""

        while r<len(num):
            st = set(num[l:r+1])
            if len(st)==1:
                largest=max(largest,num[l:r+1])
            l+=1
            r+=1

      
        return largest

