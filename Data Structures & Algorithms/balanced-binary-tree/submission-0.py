# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = 0
        self.array = [-1, 0, 1]
        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)
            if (left - right) not in self.array:
                self.res = 1
            return (max(left, right) + 1)

        depth(root)
        if self.res == 0:
            return True
        else:
            return False
