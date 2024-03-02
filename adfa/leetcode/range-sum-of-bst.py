# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []
        def inorder(cur):
            if not cur:
                return 
            inorder(cur.left)
            ans.append(cur.val)
            inorder(cur.right)
        ans.sort()
        inorder(root)
        total = 0
        for num in ans:
            if num>high:
                break
            if num>=low and num<=high:
                total +=num
        return total