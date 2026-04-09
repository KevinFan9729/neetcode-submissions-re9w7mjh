# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head) -> None:
        # let us find the middle
        slow, fast = head, head
        prev_mid = None

        while fast:
            prev_mid = slow
            slow= slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        prev_mid.next = None # cut the first portion link
        # slow now points to the start of the middle node in the linked list
        # now, let us reverse the link of the second link
        second = self.reverse(slow)
        first = head
        while second:
            tmp = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp
            first = tmp
            second = tmp2

    def reverse(self, head):
        # reverse the linked list and return the new head
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev