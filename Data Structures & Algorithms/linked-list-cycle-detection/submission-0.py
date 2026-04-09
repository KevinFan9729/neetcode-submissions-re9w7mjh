# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # can't we use a hashmap or hashet as visited?
        # if we check a node is visted, we terminate the loop and return true
        # if we finish looping, without triggering the conidtion of a node being visted return false
        # Time O(n) due to looping through the linked list
        # Space O(n) due to the set
        visited = set()

        curr = head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False
            