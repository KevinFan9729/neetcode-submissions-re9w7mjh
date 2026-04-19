"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # the key is the ramdom pointer
        # random can point to any nodes
        # while we are making the new node, we cannot just populate the random pointer
        # bec the random pointer may point to a later node that we do not have yet
            # say you are creating node 2, and random pointer points to node 6, but node 6 does not exisit yet
        # 2 passes
        # we also need a mapping of original to new 
        # this is where we pass the original node, we will get the corresponding new node
        # use a hasmap key original node, value new node 
        # Time O(n)
        # Space O(n) due toe the extra hashmap
        
        if not head:
            return None
        origToNew = {}
        currOrig = head
        # create the singly linked list nodes and populate the hashmap
        while currOrig:
            newNode = Node(currOrig.val)
            origToNew[currOrig] = newNode
            currOrig = currOrig.next

        currOrig = head
        # make the connection
        while currOrig:
            currNew = origToNew[currOrig]
            nextNew = origToNew.get(currOrig.next)
            randNew = origToNew.get(currOrig.random)
            currNew.next = nextNew
            currNew.random = randNew
            currOrig = currOrig.next
        return origToNew[head]

