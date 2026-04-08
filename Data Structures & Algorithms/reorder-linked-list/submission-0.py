# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        res = head
        arr = []
        while res:
            arr.append(res.val)
            res = res.next
        rev = arr[::-1]
        i = 0
        while head:
            head.val = arr[i]
            head = head.next
            if head:
                head.val = rev[i]
                head = head.next
            i += 1

        
        