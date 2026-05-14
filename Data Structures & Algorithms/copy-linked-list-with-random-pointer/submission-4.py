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
        res = Node(0)
        curr = head
        copy = res
        ref = dict()

        while curr:
            copy.next = Node(curr.val)
            ref[curr] = copy.next
            curr = curr.next
            copy = copy.next

        curr = head
        copy = res.next

        while curr:
            if curr.random:
                copy.random = ref[curr.random]
            curr = curr.next
            copy = copy.next

        return res.next