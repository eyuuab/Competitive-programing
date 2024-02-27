class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def helper(idx, com):
            if len(com)==k:
                ans.append(com[:])
                return
           # Calculate the maximum number that can be added to the combination
            max_num = n - (k - len(com)) + 1
            for i in range(idx, max_num + 1):
                com.append(i)
                print(com)
                helper(i+1,com)
                com.pop()
        helper(1,[])
        return ans