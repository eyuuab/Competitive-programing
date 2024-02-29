class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def backtracking(idx, com) :
            if  sum(com)==target and com not in ans:
                ans.append(com.copy())
                return 
            if sum(com)>target:
                return
            st = set()

            for i in range(idx, len(candidates)):
                if candidates[i] not in st:
                    com.append(candidates[i])
                    backtracking(i+1, com)
                    com.pop()
                    st.add(candidates[i])
        backtracking(0,[])
        return ans

