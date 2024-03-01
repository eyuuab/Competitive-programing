class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        bag = []
        for i in range(len(weights)-1):
            bag.append( weights[i] + weights[i+1] )
        bag.sort(reverse = True)
        max_, min_ = 0,0
        for i in range(k-1):
            max_+=bag[i]
            min_+=bag[-1-i]
        return max_ - min_
