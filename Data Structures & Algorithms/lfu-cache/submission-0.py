from collections import defaultdict


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1          # starts at 1, matching bucket 1
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)   # sentinel: oldest end
        self.right = ListNode(0, 0)  # sentinel: newest end
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self):
        return self.size

    def push_right(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1

    def pop(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        self.size -= 1

    def pop_left(self):
        if self.size == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.k_n = {}                           # key -> node
        self.freq_ll = defaultdict(LinkedList)  # freq -> LinkedList

    def _bump(self, node):
        freq = node.freq
        self.freq_ll[freq].pop(node)
        if freq == self.min_freq and self.freq_ll[freq].length() == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq_ll[node.freq].push_right(node)

    def get(self, key: int) -> int:
        if key not in self.k_n:
            return -1
        node = self.k_n[key]
        self._bump(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.k_n:
            node = self.k_n[key]
            node.val = value
            self._bump(node)
            return

        if len(self.k_n) == self.capacity:
            lru = self.freq_ll[self.min_freq].pop_left()
            del self.k_n[lru.key]

        node = ListNode(key, value)   # freq defaults to 1
        self.k_n[key] = node
        self.freq_ll[1].push_right(node)
        self.min_freq = 1