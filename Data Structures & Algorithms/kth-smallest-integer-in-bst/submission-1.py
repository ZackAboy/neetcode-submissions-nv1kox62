# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        stack = [root]
        while stack:
            node = stack.pop()

            heapq.heappush(heap, -node.val)

            if len(heap) > k:
                heapq.heappop(heap)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return -heapq.heappop(heap)