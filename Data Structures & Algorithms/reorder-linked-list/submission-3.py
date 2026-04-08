# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = first = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next

        second = head.next
        head.next = None
        prev = None
        while second:
            nextnode = second.next
            second.next = prev
            prev = second
            second = nextnode

        second = prev
        while second:
            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first = next1
            second = next2