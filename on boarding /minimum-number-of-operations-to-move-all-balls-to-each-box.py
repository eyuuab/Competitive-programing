class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans=[]
        ones=[]
        for i in range(n):
            if boxes[i]=='1':
                ones.append(i)
        for i in range(n):
            cnt = 0
            for  j in ones:
                cnt+=abs(j-i)
            ans.append(cnt)

        return ans