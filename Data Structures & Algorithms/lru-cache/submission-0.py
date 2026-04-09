class Node:

    def __init__(self, next = None, prev = None, value=0, key=-1):
        self.next = next
        self.key = key
        self.prev = prev
        self.val = value


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.leftDummy = Node() # least recently used
        self.rightDummy = Node() # most recently used
        self.leftDummy.next = self.rightDummy
        self.rightDummy.prev = self.leftDummy

    def remove(self, node): # remove a node bewteen left and right dummy
        prevN = node.prev
        nxtN = node.next

        prevN.next = nxtN 
        nxtN.prev = prevN
    
    def insert(self, node): # instert before the right dummy
        prevN = self.rightDummy.prev
        nxtN = self.rightDummy

        prevN.next = node
        nxtN.prev = node

        node.next = nxtN
        node.prev = prevN

    def get(self, key: int) -> int:
        if key in self.storage:
            val = self.storage[key].val
            # update the most recently used element
            # first create a new node with that value
            # second remove that node
            self.remove(self.storage[key])
            # thrid insert the node before the right dummy so it becomes the most recently used
            self.insert(self.storage[key])
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            newNode = Node(value=value, key=key)
            self.remove(self.storage[key])
            self.insert(newNode)
            self.storage[key] = newNode
            return
        if len(self.storage) < self.capacity:
            newNode = Node(value=value, key=key)
            self.insert(newNode)
            self.storage[key] = newNode
        else:
            # evict the least recently used node
            lruNode = self.leftDummy.next
            self.remove(lruNode)
            # remove the old key
            del self.storage[lruNode.key]
            # add the new node
            newNode = Node(value=value, key=key)
            self.insert(newNode)
            self.storage[key] = newNode