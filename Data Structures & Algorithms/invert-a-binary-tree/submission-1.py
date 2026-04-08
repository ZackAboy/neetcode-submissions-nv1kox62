# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        node = root

        stack = [root]

        while stack:
            node = stack.pop()
            right = node.right if node.right else None
            left = node.left if node.left else None

            if left:
                stack.append(left)

            if right:
                stack.append(right)

            node.right = left
            node.left = right

        return root


