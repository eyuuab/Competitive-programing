class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0
        while tickets[k]>0:
            for i in range(len(tickets)):
                if tickets[k]==0:
                    break
                if tickets[i]>0:
                    tickets[i]-=1
                    cnt+=1
        print(tickets)
        return cnt