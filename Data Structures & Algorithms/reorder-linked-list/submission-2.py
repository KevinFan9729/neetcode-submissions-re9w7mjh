# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # ok just to understand
            # the head node does not change
            # node that the head pointing is the last node in the original
            # then the next node is the original second node
            # then is reverse
        # omg this is very convoluted, just why?
        # one brute force way I can think of is just loop through the linked lista and
        # construct an array, and make a new linked list from the array with the desired order
        # it will be O(n) in time and space; but I guess this si not what they want

        # do I know how to reverse a linked list?
        # I do, with recursion
        # we need to find the middle (we can use fast/slow pointer)
        # once we have the middle, we will reverse the second half
        # then we will have two sub lists
        # we will alternate two lists to get the result 

        def reverse(head, prev):
            if not head:
                # after we are done with reversing
                # return the new head
                return prev
            # original next
            temp = head.next
            # reverse the link
            head.next = prev
            # to the next node
            return reverse(temp, head)
        if not head or not head.next:
            # too short, break early
            return
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # now slow is pointing at the middle node
        subhead = reverse(slow, None)
        # merge two sublists in alternating order
        head_ptr = head
        subhead_ptr = subhead
        switch = 0 
        while head_ptr and subhead_ptr:
            if switch%2 == 0:
                tmp = head_ptr.next
                head_ptr.next = subhead_ptr
                head_ptr = tmp # advance the head_ptr
            else:
                tmp = subhead_ptr.next
                subhead_ptr.next = head_ptr
                subhead_ptr = tmp # advance the subhead_ptr
            switch+=1
        if subhead_ptr: # incase that the subhead is a bit longer
            subhead_ptr.next = head_ptr
        if head_ptr: # incase that the head_ptr is a bit longer
            head_ptr.next = subhead_ptr     
        return



        