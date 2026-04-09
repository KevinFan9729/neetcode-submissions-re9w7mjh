# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we can solve this question recursively
        # reversing means we need to reverse pointers
            # currNode = head
            # nextNode = currNode.next
            # prevNode (from function)
            # reverse the link
            # currNode.next = prevNode
        
        # Time O(n) loop throuhj all nodes
        # Space O(n) due to the stack
        
        def reverse(head, prevNode):
            if not head:
                # after we are done with reversing
                # return the new head
                return prevNode
            
            currNode = head
            nextNode = head.next
            if not nextNode:
                # if we are let the last node 
                # nextNode will be None
                currNode.next = prevNode
                return reverse(None, currNode)
            else:
                temp = copy.copy(nextNode) # temp has the original next pointer for nextNode
                # reverse the link
                currNode.next = prevNode
                nextNode.next = currNode
                return reverse(temp, currNode)
        
        newhead = reverse(head, None)
        return newhead