# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def flip(cur):
            if cur is None:
                return None
            
            flipped_left = flip(cur.right)
            flipped_right = flip(cur.left)
            
            cur.left = flipped_left
            cur.right = flipped_right

            return cur
        
        root.right = flip(root.right)
        
        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        # Check if the left and right subtrees are identical
        return isSame(root.left, root.right)
