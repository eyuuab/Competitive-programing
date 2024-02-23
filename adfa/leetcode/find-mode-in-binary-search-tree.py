# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mp  = defaultdict(int)
        ans = []
        def solver(cur):
            if cur!=None:
                solver(cur.left)
                solver(cur.right)
                mp[cur.val]+=1
        solver(root)
       
        max_ = max(mp.values())
        for key, val in mp.items():
            if val==max_:
                ans.append(key)
        return ans