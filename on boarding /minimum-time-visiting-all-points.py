class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        dis = 0
        for i in range(len(points)-1):
            point = points[i]
            target = points[i+1]
            y = abs(point[1]-target[1])
            x =abs(point[0]-target[0])
            dis+=max(x,y)
        return dis
