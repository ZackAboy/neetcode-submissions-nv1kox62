# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(d, node):
            if not node:
                return d

            left_max = depth(d+1, node.left)
            right_max = depth(d+1, node.right)

            return max(left_max, right_max)

        return depth(0, root)
        