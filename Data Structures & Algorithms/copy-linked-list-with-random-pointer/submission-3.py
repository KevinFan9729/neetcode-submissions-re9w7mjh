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
        # ok the problem is this random pointer
        # we need a lookup hasmap to map the old node to new node
        # pass one we create the copy of the singly linked list
            # we also create the mapping of old to new
        # pass two we will try to create the random pointer in the new copy based
            # we loop through the old, and check the old random pointer
                # we look up the old random pointer in the hashmap to find the 
                # corresponding new node, assign the new romdan pointer
        # Time O(n) due to looping through the linked list
        # Space O(n) due to the hash map
        if head is None:
            return None
        old_to_new_map = {}
        new_head = Node(head.val)
        old_to_new_map[head] = new_head
        curr = head.next
        curr_new = new_head
        # curr_new is one step lagging behind the curr pointer
        while curr:
            new_node = Node(curr.val)
            curr_new.next = new_node
            old_to_new_map[curr] = new_node
            curr = curr.next
            curr_new = curr_new.next
        # singly linked list is done
        # now to handle the random
        curr = head
        curr_new = new_head
        while curr:
            random_old = curr.random
            random_new = old_to_new_map.get(random_old, None)
            curr_new.random = random_new
            curr = curr.next
            curr_new = curr_new.next
        return new_head