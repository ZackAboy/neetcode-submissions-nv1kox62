# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sort = ListNode()
        res = sort

        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heapq.heappop(heap)
            sort.next = node
            sort = sort.next
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, i, node))

        sort.next = None

        return res.next