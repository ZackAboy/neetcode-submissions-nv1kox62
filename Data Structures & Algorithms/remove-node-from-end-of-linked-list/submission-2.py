# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        rem = fast = dummy

        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            rem = rem.next
            fast = fast.next

        rem.next = rem.next.next

        return dummy.next