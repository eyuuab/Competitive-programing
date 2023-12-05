class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cursum = steps =0
        for i in range(len(plants)):
            cursum+=plants[i]
            if cursum>capacity:
                cursum = plants[i]
                steps +=i*2
            steps+=1
        print(steps)
        return steps
