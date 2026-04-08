# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        final = ListNode(None)
        final.next = head
        while head:
            head = head.next
            count += 1
        res = final
        for i in range(count - n):
            final = final.next
        final.next = final.next.next
        return res.next