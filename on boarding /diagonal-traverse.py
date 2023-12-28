class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        mp = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                mp[row+col].append(mat[row][col])
        for key, lst in mp.items():
            if key%2==0:
                #reverse the list 
                ans.extend(lst[::-1])
            else:
                ans.extend(lst)
        return ans