class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[0]-x[1])
        cnt = 0
        half = len(costs)//2
        for i in range(half):
            cnt+=costs[i][0]
        for i in range(half, len(costs)):
            cnt+=costs[i][1]
        return cnt