class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        def distance(point):
            x = point[0]
            y = point[1]
            return sqrt(x**2+y**2)

        for point in points:
            val = distance(point)
            dis.append((val,point))
        
        dis.sort()
        ans=[]

        for i in range(k):
            res = dis[i]
            ans.append(res[1])
        return ans