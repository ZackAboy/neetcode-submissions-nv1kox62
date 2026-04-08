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
        self.final = []
        def level(List):
            self.final.append(n.val for n in List)
            res = []
            for i in List:
                if i.left:
                    res.append(i.left)
                if i.right:
                    res.append(i.right)
            if res:
                level(res)
        level([root])
        return self.final