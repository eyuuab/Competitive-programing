class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, tw = 0,0,0
        for bill in bills:
            if bill ==5:
                five+=1
                continue
            elif five==0:
                return False
            elif bill==10:
                ten+=1
            else:
                tw+=1
            if bill ==10:
                five-=1
                
            elif bill==20:
    
                if five<3 and ten==0:
                    return False
                if ten>0:
                    ten-=1
                    five-=1
                else:
                    five-=3
                
    
        return True