# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        level_start = {} 
        def dfs(node, depth, position):
            nonlocal max_width
            if depth not in level_start:
                level_start[depth] = position
            
            max_width = max(max_width, position - level_start[depth] + 1)
            
            if node.left:
                dfs(node.left, depth + 1, 2 * position)
            
            if node.right:
                dfs(node.right, depth + 1, 2 * position + 1)
        
        dfs(root, 0, 0)
        
        return max_width