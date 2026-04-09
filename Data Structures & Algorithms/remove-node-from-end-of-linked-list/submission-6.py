# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # hmmmm we have a singly linked list and we need to remove from the end
        # the key of the problem is find that target node to be removed (actually the more important one is we stop 
         # one step previous to the node_to_del
            # we have a couple ways
                # one is to keep track of the list index in a hashmap or array then we know
                    # this method would be time O(n) and Space O(n)
                # two is do two passes
                    # first find the lenth of the linked list
                    # second find where to stop (one node before the target node) based on n and linked list length
                    # Time would be O(n) and Space O(1)
                # third is slow fast pointers
                    # have a dummy node 
                        # (actually, its always good to have a dummy for all mtheods, 
                        # to remove the edage case where we need to remove from the start)
                    # slow is starting at the dummy
                    # fast is n+1 ahead of the slow
                    # advance the both pointers until the fast is null
                    # slow.next will ne the node to be removed!
                    # Time would be O(n) and Space O(1)
        # Time O(n)
        # Space O(1)
        # Two pointers aren’t always about different speeds; sometimes they’re about a fixed distance.
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        for _ in range(n+1):
            if not fast:   # defensive; not needed if n is guaranteed valid
                return head
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        # delete
        node_to_del = slow.next
        slow.next = node_to_del.next
        node_to_del.next = None

        return dummy.next