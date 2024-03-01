# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def inorder(cur):
            if not cur:
                return None
            inorder(cur.left)
            ans.append(cur.val)
            inorder(cur.right)
        inorder(root)
        ans.sort()
        def helper(num):
            if not num:
                return None
            mid = len(num)//2
            root = TreeNode(num[mid])
            root.left = helper(num[:mid])
            root.right = helper(num[mid+1:])
            return root
        return helper(ans)
