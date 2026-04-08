# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same (a, b):
            substack = [(a, b)]
            while substack:
                a, b = substack.pop()

                if not a and not b:
                    continue

                if not a or not b:
                    return False
                
                if a.val != b.val:
                    return False

                substack.append((a.left, b.left))
                substack.append((a.right, b.right))
            return True
       
        stack = [root]

        while stack:
            node = stack.pop()
            if same(node, subRoot) is True:
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        return False

