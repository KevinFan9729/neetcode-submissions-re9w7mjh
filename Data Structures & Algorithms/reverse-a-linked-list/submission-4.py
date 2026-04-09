# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr, prev):
            if curr is None:
                return prev
            nextNode = curr.next
            curr.next = prev
            return reverse(nextNode, curr)
        a = reverse(head,None)
        return a