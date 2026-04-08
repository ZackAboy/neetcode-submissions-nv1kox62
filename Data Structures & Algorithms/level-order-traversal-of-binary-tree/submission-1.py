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
        ans = [[root.val]]

        def bfs(x):
            nonlocal ans
            
            res = deque()
            while x:
                node = x.popleft()
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
            if res:
                ans.append([i.val for i in res])
                bfs(res)

        x = deque()
        x.append(root)
        bfs(x)

        return ans