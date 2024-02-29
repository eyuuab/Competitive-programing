class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(left, right):
            if left > right:
                return None
            max_val = max(nums[left:right+1])
            max_idx = nums.index(max_val, left, right+1)
            root = TreeNode(max_val)
            root.left = helper(left, max_idx-1)
            root.right = helper(max_idx+1, right)
            return root

        return helper(0, len(nums)-1)