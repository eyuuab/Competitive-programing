class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n>45:
            return []
        ans=[]
        def backtracking(start, com):
            if len(com)==k and sum(com)==n:
                ans.append(com[:])
                return
            if sum(com)>n or len(com)>k:
                return 
            for i in range(start, 10):
                com.append(i)
                backtracking(i+1, com)
                com.pop()
        backtracking(1,[])
        return ans
