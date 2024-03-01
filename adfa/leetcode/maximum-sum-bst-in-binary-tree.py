class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def dfs(node):
            nonlocal max_sum

            if not node:
                return float('inf'), float('-inf'), 0

            left_min, left_max, left_sum = dfs(node.left)
            right_min, right_max, right_sum = dfs(node.right)

            if (
                left_max < node.val < right_min and
                left_sum != float('-inf') and
                right_sum != float('-inf')
            ):
                total_sum = left_sum + right_sum + node.val
                max_sum = max(max_sum, total_sum)
                return min(left_min, node.val), max(right_max, node.val), total_sum

            return float('-inf'), float('inf'), float('-inf')

        dfs(root)

        return max_sum