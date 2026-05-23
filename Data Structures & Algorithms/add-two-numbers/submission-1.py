# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # need to be careful of carry
        # the value at the current node is (l1+l2+carry)%10
        # the carry is (l1+l2+carry)//10
        # carry may create a new node 
        # Time O(max(n,m))
        # Space O(max(n,m))
        carry = 0
        dummy = ListNode()
        resCurr = dummy
        while l1 and l2:
            total = carry + l1.val + l2.val
            newNode = ListNode(total%10)
            resCurr.next = newNode
            resCurr = resCurr.next
            carry = total // 10
            l1=l1.next
            l2=l2.next
        while l1:
            total = carry + l1.val
            newNode = ListNode(total%10)
            resCurr.next = newNode
            resCurr = resCurr.next
            carry = total // 10
            l1=l1.next
        while l2:
            total = carry + l2.val
            newNode = ListNode(total%10)
            resCurr.next = newNode
            resCurr = resCurr.next
            carry = total // 10
            l2=l2.next
        if carry:
            newNode = ListNode(1)
            resCurr.next = newNode
            resCurr = resCurr.next
        return dummy.next