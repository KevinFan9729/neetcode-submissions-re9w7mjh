# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # feel like its more a navigation game
        # we dont know when to stop???
        # bec it is a linked list we do not know the length?
        # we can have two pointers pre and curr where they gap is n-1
        # we need to have a dummy node
        # keep moving curr and pre while maintaining the n-1 gap, and nav till curr.next = none
        # pre at this point will be at the previous of the target node
        # assume that inputs are all valid
        
        # I keep curr ahead so that when curr is at the tail, 
        #  prev.next is the nth node from the end. 
        # Since I need to delete that node in a singly linked list, 
        # landing prev one node before it lets me rewire prev.next
        # Time O(n)
        # Space O(1)
        dummy = ListNode(0, head)
        curr, prev = head, dummy
        currGap = 0
        while curr.next:
            if currGap == n-1:
                curr=curr.next
                prev=prev.next
            else:
                curr=curr.next
                currGap+=1
        # at this point we need to remove the node of prev.next
        nodeToDel = prev.next
        prev.next = nodeToDel.next
        del nodeToDel # gc will handle this when the memory cannot be accessed, but just do it for clarity
        return dummy.next