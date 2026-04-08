class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        def copy(p, q):
            stack = [(p, q)]
            while stack:
                a, b = stack.pop()
                if not a and not b:
                    continue
                if not a or not b:
                    return False
                if a.val != b.val:
                    return False
                stack.append((a.left, b.left))
                stack.append((a.right, b.right))
            return True

        stack = [root]
        while stack:
            p = stack.pop()
            q = subRoot
            if p.val == q.val:
                if copy(p, q) == True:
                    return True
            if p.left is not None:
                stack.append(p.left)
            if p.right is not None:
                stack.append(p.right)
        return False