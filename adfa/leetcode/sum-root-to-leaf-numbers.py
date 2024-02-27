# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def helper(cur, path):
            if not cur:
                return 
            path.append(path[-1]*10 +cur.val)

            if cur.left is None and cur.right is None:
                ans.append(path[:])
            helper(cur.left, path)
            helper(cur.right, path)
            path.pop()
        total  = 0
        helper(root,[0])
        for i in ans:
            total +=i[-1]
            
        return total
        