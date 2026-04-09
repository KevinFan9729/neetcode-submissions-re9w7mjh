# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr, prev):
            if not curr: # imagine at the end of the linked list
                return prev
            org_next = curr.next
            curr.next = prev
            return reverse(org_next, curr)
        node = reverse(head, None)
        return node