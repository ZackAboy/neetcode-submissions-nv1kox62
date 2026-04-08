# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        rem = res = dummy 

        for i in range(n):
            rem = rem.next

        prev = None
        while rem:
            prev = dummy
            dummy = dummy.next
            rem = rem.next

        prev.next = dummy.next

        return res.next