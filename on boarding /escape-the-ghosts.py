
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        def distance(point):
            a,b = target
            x_dist= max(a,point[0])- min(a,point[0])
            y_dist= max(b,point[1])- min(b,point[1])
            return x_dist+y_dist
            
        person = distance([0,0])
        for ghost in ghosts:
            ghostdist = distance(ghost)
            if ghostdist<=person:
                return False
        return True

       

        # dis = float('inf')
        # origin = [0, 0]
        # escap = math.dist(target, origin)

        # for i in ghosts:
        #     val = math.dist(target, i)
        #     dis = min(dis, val)

        # if dis <= escap:
        #     return False
        # else:
        #     return True