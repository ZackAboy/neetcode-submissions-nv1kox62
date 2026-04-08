# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sort = ListNode(0)
        head = sort
        while list1 and list2:
            if list1.val < list2.val:
                sort.next = list1
                sort = sort.next
                list1 = list1.next
            else:
                sort.next = list2
                sort = sort.next
                list2 = list2.next
        while list1:
            sort.next = list1
            sort = sort.next
            list1 = list1.next
        while list2:
            sort.next = list2
            sort = sort.next
            list2 = list2.next
        head = head.next
        return head