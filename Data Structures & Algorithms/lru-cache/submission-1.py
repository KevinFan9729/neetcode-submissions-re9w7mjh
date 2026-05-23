class Node:
    # doubly linked 
    def __init__(self, value=(None,None), next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:
    # LRU lesaet recently used
    # means say when the cache is full
    # we will eject item where it has gone the longest without being accessed or updated
    # so in put, if the we are at capacity 
        # we need to eject the item that has gone longest without being utlized
    # in get we need to refresh the item that it is used recently 
    # we can use a hashmap as storage
    # but the problem is the LRU part
        # Find an item by key in O(1). hashmap
        # Remove an item from the usage order and move it to the “most recently used” position in O(1) double linked list

    # hashmap: key → node in that ordering structure
    # head least recently used  <---->  ...  <---->  most recently used tail
    # we need to keep references at head and tail 
    # when inserting we insert at tail (most recently used)
    # when a key is accessed using get() or put()
    # we need to remove this node and insert at tail
    # when say we are at cpacity, we eject the item at head
    # the hashmap store key: node for fast lookup of node
    def __init__(self, capacity: int):
        self.headDummy = Node()
        self.tailDummy = Node()
        self.capacity = capacity # max size of the cache
        self.headDummy.next = self.tailDummy
        self.tailDummy.prev = self.headDummy
        self.storeMap = {}
        

    def get(self, key: int) -> int:
        # Time O(1)
        # Space O(1)
        # does not exists
        if key not in self.storeMap:
            return -1
        # exists
        # find the node
        node = self.storeMap[key]
        self.ToTail(node)
        self.storeMap[key] = node
        return node.value[1]


    def put(self, key: int, value: int) -> None:
        # Time O(1)
        # Space O(1)
        if len(self.storeMap) >= self.capacity and key not in self.storeMap:
            # need to make new room for new key
            # eject the least recently used
            # the head is the LRU
            LRU = self.headDummy.next
            # remove this head 
            self.headDummy.next = LRU.next
            LRU.next.prev = self.headDummy
            # remove from the hashmap
            del self.storeMap[LRU.value[0]]
        
        if key not in self.storeMap:
            # new node
            newNode = Node(value=(key,value))
            # add this node to the tail
            oldMRU = self.tailDummy.prev
            oldMRU.next = newNode
            newNode.prev = oldMRU
            newNode.next = self.tailDummy
            self.tailDummy.prev = newNode
            self.storeMap[key] = newNode
        else:
            # the node exists
            node = self.storeMap[key]
            self.ToTail(node)
            node.value = (key, value)
            self.storeMap[key] = node

    def ToTail(self, node):
            # this node needs to be removed and attached at the tail 
            nodeParent = node.prev
            nodeNext = node.next
            nodeParent.next = nodeNext
            nodeNext.prev = nodeParent
            # attach this node to tail
            oldMRU = self.tailDummy.prev
            oldMRU.next = node
            node.prev = oldMRU
            node.next = self.tailDummy
            self.tailDummy.prev = node

