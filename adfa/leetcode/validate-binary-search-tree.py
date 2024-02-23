# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solver(cur, min_, max_):
            if cur is None:
                return True
            if cur.val <= min_:
                return False
            if cur.val >= max_:
                return False
            return (solver(cur.left, min_, cur.val) and 
                    solver(cur.right, cur.val, max_))
        
        return solver(root, float('-inf'), float('inf'))

                