class Solution:
    def flipgame(self, fronts, backs):
        dict1, res = defaultdict(int), []

        for i,j in zip(fronts,backs):
            dict1[i] += 1
            dict1[j] += 1

        for i,j in zip(fronts,backs):
            if i == j and i in dict1:
                del dict1[i]

        return min(dict1.keys()) if dict1 else 0




        
        
        
        
        
        