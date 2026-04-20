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

        half = slow.next
        slow.next = None

        rev = None
        while half:
            nex = half.next
            half.next = rev
            rev = half
            half = nex
        
        l1 = head
        l2 = rev

        while l1 and l2:
            nex1 = l1.next
            nex2 = l2.next

            l1.next = l2
            l2.next = nex1

            l1 = nex1
            l2 = nex2
        