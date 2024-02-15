class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrow = 0
        max_end = float('-inf')
        print(points)
        for i in range(len(points)):
            start = points[i][0]
            end = points[i][1]
            if max_end>= start:
                max_end = min(max_end, end)
            else:
                arrow+=1
                max_end = end
        return arrow