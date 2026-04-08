# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []

        def bfs(x):
            nonlocal ans
            res = []
            y = deque()
            while x:
                node = x.popleft()
                res.append(node.val)
                if node.left:
                    y.append(node.left)
                if node.right:
                    y.append(node.right)
            if res:
                ans.append(res)
            if y:
                bfs(y)

        x = deque()
        x.append(root)
        bfs(x)

        return ans