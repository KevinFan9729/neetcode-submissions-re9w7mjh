# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer solution
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = left.next
        while n > 0:
            right = right.next
            n -= 1
        while right is not None:
            left = left.next
            right = right.next
        tmp = left.next.next # left.next is the node we will remove
        left.next = tmp
        return dummy.next