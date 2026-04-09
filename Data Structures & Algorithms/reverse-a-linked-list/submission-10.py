# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time O(n)
        # Space O(n)
        def reverse(curr, prev):
            if not curr:
                return prev
            next_node = curr.next
            curr.next = prev
            return reverse(next_node, curr)
        new_head = reverse(head, None)
        return new_head

        