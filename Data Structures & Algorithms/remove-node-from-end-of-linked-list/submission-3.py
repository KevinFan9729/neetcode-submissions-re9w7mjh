# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(n) in time
        # O(1) in space
        # Create a dummy node to handle edge cases easily (like removing the head) 
        # The dummy node ensures that left.next is always valid, even when removing the first node.
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = dummy
        gap = 0
        for _ in range(n):
            right= right.next # right pointer have a jump start!
        while right.next:
            right = right.next
            left = left.next
        left.next =left.next.next
        return dummy.next
        