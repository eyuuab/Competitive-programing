# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(curr, n):
            if not curr:
                return n
            l= r = 0
            if curr.left:
                l = helper(curr.left,n)
            if curr.right:
                r = helper(curr.right,n)
            return max(l,r) + 1
        return helper(root, 0)