# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def same(self, a, b):
        if not a and not b:
            return True

        if (a and not b) or (not a and b) or (a.val != b.val):
            return False

        return self.same(a.left, b.left) and self.same(a.right, b.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.same(root, subRoot) == True:
            return True

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
