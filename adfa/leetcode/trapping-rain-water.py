class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right, min_ = [0],[0],[]
        cur_max  = ans = 0
        for i in range(1,len(height)):
            cur_max = max(cur_max, height[i-1])
            max_left.append(cur_max)
        cur_max = 0
        for i in range(len(height)-2, -1,-1):
            cur_max = max(cur_max, height[i+1])
            max_right.append(cur_max)
        max_right = max_right[::-1]

        for i in range(len(height)):
            temp = min(max_left[i], max_right[i])
            if temp-height[i]>0:
                ans+= temp-height[i]
            
        return ans