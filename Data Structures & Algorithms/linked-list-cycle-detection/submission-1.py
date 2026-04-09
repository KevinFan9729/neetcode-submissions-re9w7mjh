# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we can do hare and tortoise (fast and slow ponter)
        # fast goes two nodes in one step, slow goes one node in one step
        # normally, slow ponter can never catch the fast pointer (fast will reach null first)
        # but if there is a cycle, the fast and slow pinter will meet at some ponter
        # Time O(n)
        # Space O(1)

        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow and fast!=None:
                return True
        return False
            