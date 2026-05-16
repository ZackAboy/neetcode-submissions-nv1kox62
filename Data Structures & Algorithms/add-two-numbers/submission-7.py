# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy
        carry = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1+v2+carry

            if total >=10:
                carry = 1
                total -= 10

            else:
                carry = 0
            
            dummy.next = ListNode(total)

            dummy = dummy.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

        if carry:
            dummy.next = ListNode(1)

        return res.next