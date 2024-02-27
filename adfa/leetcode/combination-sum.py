class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(com, start):
            if sum(com) == target:
                ans.append(com[:])
                return
            if sum(com) > target:
                return
            for i in range(start, len(candidates)):
                com.append(candidates[i])
                backtrack(com, i)  
                com.pop()

        backtrack([], 0)  
        return ans