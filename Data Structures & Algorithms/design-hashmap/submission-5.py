class Node:
    def __init__(self, key, val):
        self.next = None
        self.key = key
        self.val = val

class MyHashMap:
    def __init__(self):
        self.hash_table = [None] * 1000000

    def put(self, key: int, value: int) -> None:
        new_key = key % 1000000
        if self.hash_table[new_key] is None:
            self.hash_table[new_key] = Node(key, value)   
            return      
        curr = self.hash_table[new_key]
        while curr and curr.next:
            if curr.key == key:
                curr.val = value
                return
            curr = curr.next
        if curr.key == key:
            curr.val = value
            return
        curr.next = Node(key, value)
    def get(self, key: int) -> int:
        new_key = key % 1000000     
        curr = self.hash_table[new_key]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        new_key = key % 1000000
        if self.hash_table[new_key] is None:
            return 
        
        curr = self.hash_table[new_key]
        nxt = curr.next
        if not nxt:
            self.hash_table[new_key] = None
            return
        while nxt: 
            if key == nxt.key:
                curr.next = nxt.next
                return
            curr = nxt
            nxt = nxt.next
        return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)