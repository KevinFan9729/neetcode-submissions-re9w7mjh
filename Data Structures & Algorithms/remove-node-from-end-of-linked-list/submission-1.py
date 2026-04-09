# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length of the linked list
        nav = head
        length = 0
        while nav:
            length += 1
            nav = nav.next
        steps_to_move = length - n - 1
        nav = head
        while steps_to_move > 0:
            nav = nav.next
            steps_to_move -= 1
        if steps_to_move < 0:
            nav = ListNode() # dummy node
            nav.next = head
        tmp = nav.next.next # nav.next is the node we will remove
        nav.next = tmp
        if steps_to_move < 0:
            return nav.next
        return head 