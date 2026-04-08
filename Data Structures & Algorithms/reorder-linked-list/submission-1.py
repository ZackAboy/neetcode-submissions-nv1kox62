# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        p = None
        n = None
        while second:
            n = second.next
            second.next = p
            p = second
            second = n
        
        while p:
            f = first.next
            s = p.next

            first.next = p
            p.next = f

            first = f
            p = s

