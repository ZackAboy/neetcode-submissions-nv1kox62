class ListNode:
    def __init__(self, val = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()

        self.least = ListNode((-1,-1))
        self.most = ListNode((-1,-1))

        self.least.prev = None
        self.least.next = self.most

        self.most.prev = self.least
        self.most.next = None

        self.cap = capacity

    def add(self, node):
        old = self.most.prev
        old.next = node

        node.next = self.most
        self.most.prev = node

        node.prev = old

    def rem(self, node):
        prev = node.prev
        nex = node.next

        prev.next = nex
        nex.prev = prev

        node.next = None
        node.prev = None

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.rem(node)
            self.add(node)
            return node.val[1]

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.rem(node)
            del self.cache[key]

        node = ListNode((key,value))
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.cap:
            node = self.least.next
            key, val = node.val
            del self.cache[key]
            self.rem(node)