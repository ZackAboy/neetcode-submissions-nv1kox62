# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        h=[]
        for i,l in enumerate(lists):
            if l:
                
                heapq.heappush(h,(l.val,i,l))
        

        while h:
            val,i,l=heapq.heappop(h)
            curr.next=l
            if l.next:
                l=l.next
                heapq.heappush(h,(l.val,i,l))
            curr=curr.next
        return dummy.next

        
            
                