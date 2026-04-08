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
        hashset = dict()
        first = head
        copy = Node(0)
        sec = copy
        while head:
            copy.next = Node(head.val)
            hashset[head] = copy.next
            copy = copy.next
            head = head.next

        res = sec
        sec = sec.next
        while first:
            rand = hashset[first.random] if first.random else None
            sec.random = rand
            first = first.next
            sec = sec.next

        return res.next
        
