class ListNode:
    def __init__(self, val, prev = None, nex = None):
        self.val = val
        self.prev = prev
        self.next = nex

class LRUCache:

    def __init__(self, capacity: int):
        self.k = capacity
        self.cache = dict()
        self.least = ListNode((0,0))
        self.most = ListNode((0,0))
        self.least.next = self.most
        self.most.prev = self.least

    def add(self, node):
        prev = self.most.prev
        self.most.prev = node
        prev.next = node
        node.next = self.most
        node.prev = prev
    
    def remove(self, node):
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev
        node.prev = None
        node.next = None

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = (key, value)
            self.remove(node)
            self.add(node)
        else:
            node = ListNode((key, value))
            self.add(node)
            self.cache[key] = node
            if len(self.cache) > self.k:
                node = self.least.next
                self.remove(node)
                del self.cache[node.val[0]]
