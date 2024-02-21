class Solution:
    # def __init__(self, nums):
    #     self.left , self.right = 0, len(self.nums)-1
    def predictTheWinner(self, nums: List[int]) -> bool:
        # the brute force
        def yige (l,r):
            if l==r:
                return nums[l]
            score = max( nums[l]-yige(l+1,r) , nums[r]- yige(l,r-1))
            return score
        score = yige(0,len(nums)-1)
        return True if score>=0 else False