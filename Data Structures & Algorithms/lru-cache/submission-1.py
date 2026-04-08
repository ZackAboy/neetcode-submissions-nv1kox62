class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()

        self.least = ListNode(0, 0)
        self.most = ListNode(0, 0)

        self.least.next = self.most
        self.most.prev = self.least

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prevmost = self.most.prev

        prevmost.next = node
        node.prev = prevmost

        node.next = self.most

        self.most.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old = self.cache[key]
            self.remove(old)
        new = ListNode(key, value)
        self.cache[key] = new
        self.insert(new)
        if len(self.cache) > self.cap:
            lru = self.least.next
            self.remove(lru)
            del self.cache[lru.key]
                    
