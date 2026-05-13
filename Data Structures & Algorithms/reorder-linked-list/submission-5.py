# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we need to first find out the length of the linked list
        # then we cut the linked list into 2 halfs at n/2
        # we reverse the second half
        # then insert nodes from the second half into the first half alternatively
        # we dont need to find the length, what we need is actually the mid point
            # we can do so by fast and slow pointer 
            # fast pointer moves 2 step and slow pointer move 1 step
            # one fast is null, slow will be at mid
        # Time O(n)
        # Space O(1)
        
        fast, slow = head, head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            slow = slow.next
        
        part1Head = head
        part2Head = slow.next
        # sever the link into 2 pieces
        slow.next = None
        # we make part1 longer as we want to make sure part2 can be exhausted before we run out nodes in part1
        def reverse(head, prev):
            while head:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            return prev
        reversedP2H = reverse(part2Head, None)

        curr1 = part1Head
        curr2 = reversedP2H
        while reversedP2H:
            next1 = curr1.next
            curr1.next = curr2
            reversedP2H = reversedP2H.next # save/access next node in second half BEFORE overwriting curr2.next
            curr2.next = next1
            curr1 = next1
            curr2 = reversedP2H
