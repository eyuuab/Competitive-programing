# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]: 
        column_map = defaultdict(list)

        def dfs(node, row, column):
            if node is None:
                return
            column_map[column].append((row, node.val))

            dfs(node.left, row + 1, column - 1)
            dfs(node.right, row + 1, column + 1)

        dfs(root, 0, 0)

        ans = []
        for column in sorted(column_map):
            temp = []
            for row, value in column_map[column]:
                heappush(temp, (row, value))

            column_nodes = []
            while temp:
                column_nodes.append(heappop(temp)[1])

            ans.append(column_nodes)

        return ans