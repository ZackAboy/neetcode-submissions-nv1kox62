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
        copy = Node(0)
        pointer = {}

        curr = head
        currcopy = copy
        while curr:
            currcopy.next = Node(curr.val)
            pointer[curr] = currcopy.next
            curr = curr.next
            currcopy = currcopy.next

        curr = head
        currcopy = copy.next

        while curr:
            if curr.random:
                currcopy.random = pointer[curr.random]
            curr = curr.next
            currcopy = currcopy.next

        return copy.next