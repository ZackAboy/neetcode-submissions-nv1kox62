# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def recur(root):
            if not root:
                return 0

            leftmax = recur(root.left)
            rightmax = recur(root.right)
            leftmax = max(0, leftmax)
            rightmax = max(0, rightmax)

            self.res = max(self.res, (leftmax + rightmax + root.val))

            return root.val + max(leftmax, rightmax)

        recur(root)
        return self.res
        