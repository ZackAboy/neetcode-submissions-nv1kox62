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
        ans = Node(0)
        res = ans
        rand = {}
        while head:
            ans.next = Node(head.val)
            rand[head] = ans.next
            ans = ans.next
            head = head.next
        for val, clone in rand.items():
            if val.random:
                clone.random = rand[val.random]
            else:
                clone.random = None
        return res.next