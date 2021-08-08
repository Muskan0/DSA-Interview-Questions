# https://leetcode.com/problems/lru-cache/

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        
        self.head=Node(-1, -1)
        self.tail=Node(-1,-1)
        
        self.head.next=self.tail
        self.tail.prev=self.head
        self.map=dict()
        
    def add(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next=node
        node.next.prev=node
    
    def delete(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev
        
    def get(self, key: int) -> int:
        if key in self.map:
            node=self.map[key]
            self.delete(self.map[key])
            self.add(node)

            self.map[key]=node
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.delete(self.map[key])
            del self.map[key]
        elif len(self.map)==self.capacity:
            del self.map[self.tail.prev.key]
            self.delete(self.tail.prev)

        node=Node(key,value)
        self.add(node)
        self.map[key]=node
        
        
class Node:
    def __init__(self, key, value):
        self.value=value
        self.key=key
        self.prev=None
        self.next=None
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
