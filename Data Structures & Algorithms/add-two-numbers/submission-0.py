# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # need to worry about the carry bit 
        # also I guess l1 and l2 can be different size
        # Time O(n)
        # Space O(1) if not counting output
        curr1 = l1
        curr2 = l2
        # dummy = ListNode() # dummy
        res_head = ListNode()
        res_curr = res_head
        res_prev = None
        while curr1 or curr2:
            if curr1:
                num1 = curr1.val
                curr1 = curr1.next
            else:
                num1 = 0
            if curr2:
                num2 = curr2.val
                curr2 = curr2.next
            else:
                num2 = 0
            curr_sum = num1 + num2 + res_curr.val
            curr_val = curr_sum % 10
            carry = curr_sum // 10 
            res_curr.val = curr_val
            next_res_node = ListNode(carry)
            res_curr.next = next_res_node
            res_prev = res_curr # use to delete leading zero
            res_curr = res_curr.next
        # get rid of leading zero
        if res_curr.val == 0:
            if res_prev:
                res_prev.next = None
        return res_head