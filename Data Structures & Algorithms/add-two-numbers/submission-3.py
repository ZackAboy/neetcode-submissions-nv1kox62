# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode()
        ans = res

        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            val = a + b + carry

            if val>=10:
                res.next = ListNode(val-10)
                carry = 1
            else:
                res.next = ListNode(val)
                carry = 0

            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            res.next = ListNode(1)

        return ans.next