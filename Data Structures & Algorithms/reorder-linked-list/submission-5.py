# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l2 = head
        dummy = head

        while dummy and dummy.next:
            l2 = l2.next
            dummy = dummy.next.next

        l1 = l2.next
        l2.next = None

        prev = None
        while l1:
            nex = l1.next
            l1.next = prev
            prev = l1
            l1 = nex
        
        l2 = prev
        l1 = head

        while l1 and l2:
            nex1 = l1.next
            nex2 = l2.next

            l1.next = l2
            l2.next = nex1

            l1 = nex1
            l2 = nex2
        