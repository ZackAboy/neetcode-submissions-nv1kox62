# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p2 = slow.next
        slow.next = None
        p1 = head
        prev = None
        while p2:
            nex = p2.next
            p2.next = prev
            prev = p2
            p2 = nex
        p2 = prev
        while p1 and p2:
            nex1 = p1.next
            nex2 = p2.next

            p1.next = p2
            p2.next = nex1

            p1 = nex1
            p2 = nex2