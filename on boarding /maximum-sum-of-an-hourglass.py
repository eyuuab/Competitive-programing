class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)-2):
            first = grid[i]
            second = grid[i+1]
            third = grid[i+2]
            print(first, second,third)
            for j in range(len(first)-2):
                a = first[j] +first[j+1] + first[j+2]
                b = second [j+1]
                c= third[j] +third[j+1] + third [j+2]
                ans = max(ans, (a+b+c))
        return ans