class Solution:
    def reverseStr(self, s: str, k: int) -> str:
      
        mylist = list(s)
        
        for i in range(0, len(mylist), k + k):
         
            mylist[i:k + i] = reversed(mylist[i:k + i])
            
       
        return "".join(mylist)