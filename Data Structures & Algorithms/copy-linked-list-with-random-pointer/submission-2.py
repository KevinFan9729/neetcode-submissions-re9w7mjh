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
        # O(n)
        if not head: # length 0 linked list
            return head
        randomindexMap = {}
        nav = head 
        index = 0
        while nav:
            randomindexMap[nav] = index
            nav = nav.next
            index += 1
        nav = head
        array = []
        while nav:
            node = Node(nav.val)
            array.append(node)
            nav = nav.next
        nav = head
        index = 0
        while nav:
            curr = array[index]
            if index +1 < len(array):
                nextNode = array[index+1]
            else:
                nextNode = None
            curr.next = nextNode
            randomNodeIndex = randomindexMap.get(nav.random, None)
            if randomNodeIndex is not None:
                randomNode = array[randomNodeIndex]
            else:
                randomNode = None
            curr.random = randomNode
            nav = nav.next
            index += 1
        return array[0]