class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.c={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    def rem(self,node):
        prevv=node.prev
        nextt=node.next
        prevv.next=nextt
        nextt.prev=prevv
    def insert(self,node):
        prevv=self.right.prev
        nextt=self.right
        prevv.next=node
        node.prev=prevv
        node.next=nextt
        nextt.prev=node        

    def get(self, key: int) -> int:
        if key not in self.c:
            return -1
        node=self.c[key]
        self.rem(node)
        self.insert(node)
        return node.val


        

    def put(self, key: int, value: int) -> None:
        if key in self.c:
            self.rem(self.c[key])
        node=Node(key,value)
        self.c[key]=node
        self.insert(node)
        if len(self.c)>self.capacity:
            lru=self.left.next
            self.rem(lru)
            del self.c[lru.key]

        
