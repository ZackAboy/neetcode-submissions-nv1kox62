# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        sec = slow.next
        slow.next = None

        rev = None
        while sec:
            nex = sec.next
            sec.next = rev
            rev = sec
            sec = nex

        while rev:
            tmp1 = head.next
            tmp2 = rev.next

            head.next = rev
            rev.next = tmp1

            head = tmp1
            rev = tmp2