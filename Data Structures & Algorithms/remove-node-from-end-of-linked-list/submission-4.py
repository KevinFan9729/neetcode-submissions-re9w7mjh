# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # hmmmm we have a singly linked list and we need to remove from the end
        # the key of the problem is find that target node to be removed
            # how?
            # we could just tervse the linked list and maintain a hash map
            # the hash map has value as the reference for the node
            # key as the number from the end (1-indexed)
        # Time O(n)
        # Space O(n)
        count = 0
        count_map = {}
        curr = head
        while curr:
            count_map[count] = curr
            count += 1
            curr  = curr.next
        # the real index at (1-indexed) can be computed as n = (map value - (count))*-1
        # here the count is the real length of the linked list
        # n is counting from the end
        # as n = (map value - (count))*-1
        # n = -map value + count
        # map value = count - n
        target_val = count - n
        if target_val not in count_map:
            return head
        prev_node_n = n + 1
        target_prev_val = count - prev_node_n
        node_to_del = count_map[target_val]
        if target_prev_val not in count_map:
            # if no previous, it means we are deleting from the front
            head = node_to_del.next
            node_to_del = None 
            return head
        prev_node = count_map[target_prev_val]

        # delete the node
        prev_node.next = node_to_del.next
        node_to_del.next = None

        return head
