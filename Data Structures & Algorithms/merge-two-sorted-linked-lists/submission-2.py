# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers
        # one for the list1 one for list2
        # two lists are sorted
        # dummy node for the final list to track the new head
        # we always point to the samllest node 
        # if pt1 < pt2
        # nextnode is pt1
        # move pt1 to pt1.next
        # if pt1 >= pt2
        # nextnode is pt2
        # move pt2 to pt2.next
        #if we run out of node in one list
        # append the reminder to the final list as lists are sorted
        # Time O(n+m) as we need to traverse all nodes
        # Space O(1) if not counting return size
        dummy =  ListNode(-999)
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                # nextNode = ListNode(list1.val)
                nextNode = list1
                curr.next = nextNode
                list1=list1.next
            else:
                # nextNode = ListNode(list2.val)
                nextNode = list2
                curr.next = nextNode
                list2=list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next