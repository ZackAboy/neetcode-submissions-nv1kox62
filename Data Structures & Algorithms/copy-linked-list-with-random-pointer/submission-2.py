"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy=Node(0)

        copy=dummy
        curr=head
        oldtocopy={}
        while curr:
            copy.next=Node(curr.val)
            oldtocopy[curr]=copy.next
            curr=curr.next
            copy=copy.next


        curr=head
        copy=dummy.next
        while curr:
            if curr.random:
                copy.random=oldtocopy[curr.random]
            curr=curr.next
            copy=copy.next
        return dummy.next
