# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast and slow pointer?
        # fast pointer move two steps
        # slow pointer move one step
        # when fast pointer runs out, the slow pointer will be at the middle
        # why is this?
        # bec the fast pointer is twice as the speed of the slow
        # when fast pointer is done, slow pointer will point to the middle
        # Time O(n)
        # Space O(1)

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
        