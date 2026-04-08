# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maz):
            if not node:
                return 0

            good = 1 if node.val>=maz else 0
            maz = max(maz, node.val)

            return good + dfs(node.left, maz) + dfs(node.right, maz)

        return dfs(root, root.val)