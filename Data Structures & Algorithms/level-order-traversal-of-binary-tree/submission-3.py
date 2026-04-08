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
        res = [[root.val]]

        def bfs(curr):
            q = deque()
            while curr:
                node = curr.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(q)>0:
                app = [i.val for i in q]
                res.append(app)
                bfs(q)
        
        q = deque()
        q.append(root)
        bfs(q)

        return res


        
