# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(None)
        l1val = []
        while l1:
            l1val.append(l1.val)
            l1 = l1.next
        l2val = []
        while l2:
            l2val.append(l2.val)
            l2 = l2.next
        l1val.reverse()
        l2val.reverse()
        l1 = 0
        l2 = 0
        for i in l1val:
            l1 = l1*10 + i
        for i in l2val:
            l2 = l2*10 + i
        resval = [int(c) for c in str(int(l1+l2))]
        resval.reverse()
        ans = res
        for val in resval:
            res.next = ListNode(val)
            res = res.next
        return ans.next