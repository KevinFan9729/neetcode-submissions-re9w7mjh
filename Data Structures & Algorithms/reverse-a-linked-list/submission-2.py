# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr, prev):
            if curr is None: # imagine at the end of the linked list
                return prev
            else:
                next = curr.next
                curr.next = prev
                return reverse(next, curr) # use the recursion call stack to get the previous pointer
            
        return reverse(head, None)
