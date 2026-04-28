# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow ptr we can detect cycle!
        # if fast meet slow, it means we have a cycle
        # if they do not meet, it means no cycle
        # Time O(n)
        # Space O(1)
        slow, fast = head, head
        while fast:
            if slow:
                slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                # this means that fast can run out
                # no cycel
                return False
            if slow == fast:
                return True

        return False