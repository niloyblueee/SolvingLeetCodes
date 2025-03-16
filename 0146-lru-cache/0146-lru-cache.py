class Node:

    def __init__(self, key , val):
        self.val , self.next, self.prev = val, None, None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.hash = {}

        self.left , self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node



    def remove(self,node):
        next, prev = node.next, node.prev
        prev.next = next 
        next.prev = prev 

    def get(self, key: int) -> int:
        
        if key in self.hash:
            self.remove(self.hash[key])
            self.insert(self.hash[key])
            return self.hash[key].val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])
        
        self.hash[key] = Node(key, value)
        self.insert(self.hash[key])
        
        if len(self.hash) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.hash[LRU.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)