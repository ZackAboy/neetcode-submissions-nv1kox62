# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d = 0
        def depth(d, node):
            if not node:
                return d
            
            l_max = depth(d+1, node.left)
            r_max = depth(d+1, node.right)

            return max(l_max, r_max)
        return depth(0, root)